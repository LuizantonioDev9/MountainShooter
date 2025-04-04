from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.PlayerShot import PlayerShot
from code.const import WIN_WIDTH


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity): # se o inimigo passar da tela a vida dele chega a zero
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot): # verificar se o tiro do player passar da tela, para ser destruido tbm, pq ele conta como entidade
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0




    @staticmethod
    def verify_collision(entity_list: list[Entity]): # recebe todas as entidades
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]): # com a vida em zero vamos remover ele da lista
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)