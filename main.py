from abc import ABC, abstractmethod
import random

# Создаем абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Создаем класс мечей
class Sword(Weapon):
    def attack(self):
        damage = random.randint(8, 15)
        print(f"Боец наносит удар мечом, нанося {damage} урона!")
        return damage
# Создаем класс лука
class Bow(Weapon):
    def attack(self):
        damage = random.randint(5, 10)
        print(f"Боец стреляет из лука, нанося {damage} урона!")
        return damage

# Класс  монстра
class Monster:
    def __init__(self, health):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Монстр побежден!")
        else:
            print(f"Монстр остался с {self.health} здоровья.")

# Модифицируем класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__.lower()}.")

    def attack_monster(self, monster):
        if self.weapon:
            damage = self.weapon.attack()
            monster.take_damage(damage)
        else:
            print(f"{self.name} не имеет оружия для атаки!")

#  Реализация боя
def main():
    # Создаем бойца и монстра
    fighter = Fighter("Боец")
    monster = Monster(20)  # Монстр с 20 здоровьем

    # Бой с мечом
    sword = Sword()
    fighter.change_weapon(sword)
    fighter.attack_monster(monster)

    # Бой с луком
    bow = Bow()
    fighter.change_weapon(bow)
    fighter.attack_monster(monster)

if __name__ == "__main__":
    main()