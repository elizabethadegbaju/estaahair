from django.utils.translation import ugettext_lazy as _
from decimal import Decimal as D
from oscar.core import prices
from oscar.apps.shipping import methods


# class Reserve(methods.NoShippingRequired):
#     code = 'RESERVE'
#     name = 'Reserve'
#     description = 'Items will be reserved at the warehouse for 7 days'


class OutsideNigeria(methods.Base):
    """
        This shipping method indicates that shipping costs a fixed price and
        requires no special calculation.
        """
    code = 'outside nigeria'
    name = _('Outside Nigeria')
    description = 'Please select this method if you reside outside Nigeria.'

    # Charges can be either declared by subclassing and overriding the
    # class attributes or by passing them to the constructor
    charge_excl_tax = None
    charge_incl_tax = None

    def __init__(self, charge_excl_tax = D('38.57'), charge_incl_tax = D('38.57')):
        if charge_excl_tax is not None:
            self.charge_excl_tax = charge_excl_tax
        if charge_incl_tax is not None:
            self.charge_incl_tax = charge_incl_tax

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax,
            incl_tax=self.charge_incl_tax)


class OtherStates(methods.Base):
    """
        This shipping method indicates that shipping costs a fixed price and
        requires no special calculation.
        """
    code = 'other-states-in-nigeria'
    name = _('Other States Within Nigeria')
    description = 'Please select this method if you live within Nigeria and outside Lagos'

    # Charges can be either declared by subclassing and overriding the
    # class attributes or by passing them to the constructor
    charge_excl_tax = None
    charge_incl_tax = None

    def __init__(self, charge_excl_tax = D('7.14'), charge_incl_tax = D('7.14')):
        if charge_excl_tax is not None:
            self.charge_excl_tax = charge_excl_tax
        if charge_incl_tax is not None:
            self.charge_incl_tax = charge_incl_tax

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax,
            incl_tax=self.charge_incl_tax)


class LagosIsland(methods.Base):
    """
        This shipping method indicates that shipping costs a fixed price and
        requires no special calculation.
        """
    code = 'lagos-island'
    name = _('Lagos Island')
    description = 'Please select this method if you live on the Island'

    # Charges can be either declared by subclassing and overriding the
    # class attributes or by passing them to the constructor
    charge_excl_tax = None
    charge_incl_tax = None

    def __init__(self, charge_excl_tax = D('4.29'), charge_incl_tax = D('4.29')):
        if charge_excl_tax is not None:
            self.charge_excl_tax = charge_excl_tax
        if charge_incl_tax is not None:
            self.charge_incl_tax = charge_incl_tax

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax,
            incl_tax=self.charge_incl_tax)


class LagosMainland(methods.Base):
    """
        This shipping method indicates that shipping costs a fixed price and
        requires no special calculation.
        """
    code = 'lagos-mainland'
    name = _('Lagos Mainland')
    description = 'Please select this method if you live on the mainland'

    # Charges can be either declared by subclassing and overriding the
    # class attributes or by passing them to the constructor
    charge_excl_tax = None
    charge_incl_tax = None

    def __init__(self, charge_excl_tax = D('2.86'), charge_incl_tax = D('2.86')):
        if charge_excl_tax is not None:
            self.charge_excl_tax = charge_excl_tax
        if charge_incl_tax is not None:
            self.charge_incl_tax = charge_incl_tax

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax,
            incl_tax=self.charge_incl_tax)


class PickUpIkeja(methods.NoShippingRequired):
    """
        This shipping method indicates that shipping costs nothing as the customer will pick up by herself from the
        shop in Ikeja.
        """
    code = 'pick-up-ikeja'
    name = _('Pick Up from Ikeja Station')
    description = 'Items will be reserved for 7 days after order. Please ensure to pick up within the time limit'