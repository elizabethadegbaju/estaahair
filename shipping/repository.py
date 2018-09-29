from shipping import methods as oldmethods
from oscar.apps.shipping import repository
from oscar.core.loading import get_classes

(Free, NoShippingRequired,
 TaxExclusiveOfferDiscount, TaxInclusiveOfferDiscount, OutsideNigeria, LagosIsland, LagosMainland, OtherStates,
 PickUpIkeja) \
    = get_classes('shipping.methods', ['Free', 'NoShippingRequired',
                                       'TaxExclusiveOfferDiscount', 'TaxInclusiveOfferDiscount', 'OutsideNigeria',
                                       'LagosIsland', 'LagosMainland', 'OtherStates', 'PickUpIkeja'])

class Repository(repository.Repository):

    def get_available_shipping_methods(
            self, basket, user=None, shipping_addr=None,
            request=None, **kwargs):
        if shipping_addr and shipping_addr.country.code == 'NG':
            # Express is only available in Nigeria
            methods = ( oldmethods.PickUpIkeja(), oldmethods.LagosMainland(), oldmethods.LagosIsland(),
                        oldmethods.OtherStates())
        else:
            methods = (oldmethods.OutsideNigeria(),)
        return methods

