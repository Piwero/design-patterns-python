class FlyBehaviour:
    def fly(self):
        raise NotImplementedError


class FlyWithWings(FlyBehaviour):
    def fly(self):
        print("I'm flying!!")


class FlyNoWay(FlyBehaviour):
    def fly(self):
        print("I can't fly")


class FlyRocketPowered(FlyBehaviour):
    def fly(self):
        print("I'm flying with a rocket!'")


class QuackBehaviour:
    def quack(self):
        raise NotImplementedError


class Quack(QuackBehaviour):
    def quack(self):
        print("Quack")


class MuteQuack(QuackBehaviour):
    def quack(self):
        print("<< Silence >>")


class Squeak(QuackBehaviour):
    def quack(self):
        print("Squeak")


class Duck:
    _fly_Behaviour = None
    _quack_Behaviour = None

    def set_fly_Behaviour(self, fly_Behaviour):
        self._fly_Behaviour = fly_Behaviour

    def set_quack_Behaviour(self, quack_Behaviour):
        self._quack_Behaviour = quack_Behaviour

    def display(self):
        raise NotImplementedError

    def perform_fly(self):
        self._fly_Behaviour.fly()

    def perform_quack(self):
        self._quack_Behaviour.quack()

    def swim(self):
        print("All ducks float, even decoys!")


class MallardDuck(Duck):
    _fly_Behaviour = FlyWithWings()
    _quack_Behaviour = Quack()

    def display(self):
        print("I'm a real Mallard duck")


class DecoyDuck(Duck):
    _fly_Behaviour = FlyNoWay()
    _quack_Behaviour = MuteQuack()

    def display(self):
        print("I'm a duck Decoy")


class ModelDuck(Duck):
    _fly_Behaviour = FlyNoWay()
    _quack_Behaviour = Squeak()

    def display(self):
        print("I'm a real Mallard duck")


class RedHeadDuck(Duck):
    _fly_Behaviour = FlyWithWings()
    _quack_Behaviour = Quack()

    def display(self):
        print("I'm a real Red Headed duck")


class RubberDuck(Duck):
    _fly_Behaviour = FlyNoWay()
    _quack_Behaviour = Squeak()

    def display(self):
        print("I'm a rubber duckie")


def mini_duck_simulator():
    print("Mallard Duck Simulator")
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()
    print("Model Duck Simulator")
    model = ModelDuck()
    model.perform_fly()
    model.set_fly_Behaviour(FlyRocketPowered())
    model.perform_fly()


if __name__ == "__main__":
    mini_duck_simulator()
