
#In this example, I defined two concrete pricing strategies (FixedPriceStrategy and MarketDrivenStrategy)
# representing different approaches to pricing properties. The Property class acts as the context class
# that maintains the current pricing strategy and calculates the price based on the selected strategy.
# The PricingStrategy interface ensures that all concrete strategies implement the calculate_price() method,
# allowing for seamless switching between strategies

from abc import ABC, abstractmethod


# Interface for pricing strategy
class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, property_details):
        pass


# Concrete implementation of Fixed Price Strategy
class FixedPriceStrategy(PricingStrategy):
    def calculate_price(self, property_details):
        return property_details['base_price']  # Fixed price regardless of market conditions


# Concrete implementation of Market Driven Strategy
class MarketDrivenStrategy(PricingStrategy):
    def calculate_price(self, property_details):
        market_demand = property_details['market_demand']
        base_price = property_details['base_price']

        # Adjust price based on market demand
        if market_demand == 'high':
            return base_price * 1.2  # Increase price by 20% for high demand
        elif market_demand == 'low':
            return base_price * 0.8  # Decrease price by 20% for low demand
        else:
            return base_price  # Keep the base price unchanged for normal demand


# Context class representing the property
class Property:
    def __init__(self, pricing_strategy):
        self._pricing_strategy = pricing_strategy

    def set_pricing_strategy(self, pricing_strategy):
        self._pricing_strategy = pricing_strategy

    def calculate_price(self, property_details):
        return self._pricing_strategy.calculate_price(property_details)


# Example usage
if __name__ == "__main__":
    # Create property with initial pricing strategy
    property1 = Property(FixedPriceStrategy())

    # Property details
    property_details = {
        'base_price': 1000000,
        'market_demand': 'high'
    }

    # Calculate price using current strategy
    print("Price using Fixed Price Strategy:", property1.calculate_price(property_details))

    # Switch to Market Driven Strategy
    property1.set_pricing_strategy(MarketDrivenStrategy())

    # Calculate price using new strategy
    print("Price using Market Driven Strategy:", property1.calculate_price(property_details))
