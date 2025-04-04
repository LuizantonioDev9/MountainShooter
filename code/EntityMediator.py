from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot
from code.const import WIN_WIDTH


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):  # se o inimigo passar da tela a vida dele chega a zero
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent,
                      PlayerShot):  # verificar se o tiro do player passar da tela, para ser destruido tbm, pq ele conta como entidade
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot': # se o tiro final é do player 1
            for ent in entity_list: # vou varrer a lista e achar o player 1 e da o score para ele
                if ent.name == 'Player1':
                    ent.score += enemy.score

        if enemy.last_dmg == 'Player2Shot': # se o tiro final é do player 1
            for ent in entity_list: # vou varrer a lista e achar o player 1 e da o score para ele
                if ent.name == 'Player2':
                    ent.score += enemy.score

    @staticmethod
    def __verify_collision_entity(ent1, ent2):  # verifica colisão de tiro com nave
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:  # if valid_interaction == True:
            if (ent1.rect.right >= ent2.rect.left and # verifica se houve colição fisica das naves
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod  # verifica as colisoes
    def verify_collision(entity_list: list[Entity]):  # recebe todas as entidades
        # verificar se as classes se colidem sem por exemplo: player1 colide com player1? não tem redundancia nesse cod abaixo
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):  # com a vida em zero vamos remover ele da lista
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent,entity_list) # que player ou inimigo matou oq da lista
                entity_list.remove(ent)
