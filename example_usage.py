"""
Example usage of the size converter module
This script demonstrates how to use all functions from the size_converter module
"""

from size_converter import *

def main():
    print("Welcome to the Size Converter Demo!")
    print("-" * 40)
    
    # Example 1: Using get_measurements() for interactive input
    print("\nExample 1: Getting measurements interactively")
    print("Please enter your measurements when prompted:")
    measurements = get_measurements()
    
    if measurements:
        print("\nYour measurements:", measurements)
        
        # Example 2: Getting dress size
        dress_size = get_dress_size(measurements)
        print("\nExample 2: Dress Size")
        print(f"Your US dress size: {dress_size}")
        
        # Example 3: Getting pant size
        pant_size = get_pant_size(measurements)
        print("\nExample 3: Pant Size")
        print(f"Your US pant size: {pant_size}")
        
        # Example 4: Getting top size
        top_size = get_top_size(measurements)
        print("\nExample 4: Top Size")
        print(f"Your US top size: {top_size}")
        
        # Example 5: Converting shoe size
        shoe_sizes = convert_shoe_size(measurements['shoe_size'])
        print("\nExample 5: Shoe Size Conversions")
        print(f"US size: {shoe_sizes['US']}")
        print(f"EU size: {shoe_sizes['EU']}")
        print(f"UK size: {shoe_sizes['UK']}")
        
        # Example 6: Converting clothing sizes to international sizes
        print("\nExample 6: International Size Conversions")
        
        # Dress size conversions
        int_dress_sizes = convert_clothing_size(dress_size, 'dress')
        print("\nDress Sizes:")
        print(f"US: {int_dress_sizes['US']}")
        print(f"French: {int_dress_sizes['FR']}")
        print(f"Italian: {int_dress_sizes['IT']}")
        print(f"UK: {int_dress_sizes['UK']}")
        
        # Top size conversions
        int_top_sizes = convert_clothing_size(top_size, 'top')
        print("\nTop Sizes:")
        print(f"US: {int_top_sizes['US']}")
        print(f"French: {int_top_sizes['FR']}")
        print(f"Italian: {int_top_sizes['IT']}")
        print(f"UK: {int_top_sizes['UK']}")
        
        # Pant size conversions
        int_pant_sizes = convert_clothing_size(pant_size, 'pant')
        print("\nPant Sizes:")
        print(f"US: {int_pant_sizes['US']}")
        print(f"French: {int_pant_sizes['FR']}")
        print(f"Italian: {int_pant_sizes['IT']}")
        print(f"UK: {int_pant_sizes['UK']}")

if __name__ == "__main__":
    main()
