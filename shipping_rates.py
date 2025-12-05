"""
Shipping Logistics Rate Calculator
----------------------------------
Starter code for calculating shipping costs based on:
- Package weight
- Distance
- Shipping speed
- Carrier multipliers

This module is designed for extension by contributors.
"""

# Default rate constants (may be updated with real business data)
BASE_RATE_PER_KG = 1.20          # base cost per kg
BASE_RATE_PER_KM = 0.05          # base cost per kilometer
SPEED_MULTIPLIERS = {
    "standard": 1.0,
    "express": 1.5,
    "overnight": 2.0,
}
CARRIER_MULTIPLIERS = {
    "generic": 1.0,
    "fastship": 1.2,
    "economyfreight": 0.9,
}


def calculate_shipping_rate(
    weight_kg: float,
    distance_km: float,
    speed: str = "standard",
    carrier: str = "generic"
) -> float:
    """
    Calculate the cost of shipping a package.

    Parameters:
        weight_kg (float): Weight of the package in kilograms.
        distance_km (float): Distance to ship in kilometers.
        speed (str): Shipping speed. Options: standard, express, overnight.
        carrier (str): Carrier option. Defined in CARRIER_MULTIPLIERS.

    Returns:
        float: Calculated shipping rate in dollars.

    Raises:
        ValueError: If inputs are invalid or unsupported.
    """
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than 0 kg.")

    if distance_km <= 0:
        raise ValueError("Distance must be greater than 0 km.")

    if speed not in SPEED_MULTIPLIERS:
        raise ValueError(f"Unsupported speed option: {speed}")

    if carrier not in CARRIER_MULTIPLIERS:
        raise ValueError(f"Unsupported carrier: {carrier}")

    weight_cost = weight_kg * BASE_RATE_PER_KG
    distance_cost = distance_km * BASE_RATE_PER_KM
    base_cost = weight_cost + distance_cost

    # Apply multipliers
    cost_with_speed = base_cost * SPEED_MULTIPLIERS[speed]
    final_cost = cost_with_speed * CARRIER_MULTIPLIERS[carrier]

    return round(final_cost, 2)


def main():
    """Simple CLI for manual testing."""
    print("Shipping Logistics Rate Calculator")

    try:
        weight = float(input("Enter package weight (kg): "))
        distance = float(input("Enter distance (km): "))
        speed = input("Enter speed (standard/express/overnight): ").strip().lower()
        carrier = input("Enter carrier (generic/fastship/economyfreight): ").strip().lower()

        rate = calculate_shipping_rate(weight, distance, speed, carrier)
        print(f"\nEstimated Shipping Cost: ${rate}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
