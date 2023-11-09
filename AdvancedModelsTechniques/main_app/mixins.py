class RechargeEnergyMixin:

    def recharge_energy(self, amount: int) -> None:
        self.energy += amount

        if self.energy > 100:
            self.energy = 100

        self.save()