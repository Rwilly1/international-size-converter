"""
Size Converter Module
This module provides functions for converting various clothing and shoe sizes
between different international sizing systems.
"""

def get_measurements():
    """
    Get user measurements interactively.
    
    Returns:
        dict: Dictionary containing user measurements (bust, waist, hips in inches,
              and shoe size in US sizing)
    """
    measurements = {}
    try:
        measurements['bust'] = float(input("Enter bust measurement (inches): "))
        measurements['waist'] = float(input("Enter waist measurement (inches): "))
        measurements['hips'] = float(input("Enter hips measurement (inches): "))
        measurements['shoe_size'] = float(input("Enter US shoe size: "))
        return measurements
    except ValueError:
        print("Please enter valid numerical measurements.")
        return None

def get_dress_size(measurements):
    """
    Convert body measurements to US dress size.
    
    Args:
        measurements (dict): Dictionary containing bust, waist, and hips measurements
    
    Returns:
        int: US dress size
    """
    if not all(key in measurements for key in ['bust', 'waist', 'hips']):
        return None
        
    # Using waist measurement as primary indicator for dress size
    waist = measurements['waist']
    
    # Basic US dress size conversion chart
    size_chart = {
        24: 0,
        25: 2,
        26: 4,
        27.5: 6,
        29: 8,
        30.5: 10,
        32: 12,
        34: 14,
        36: 16,
        38: 18,
        40: 20
    }
    
    # Find the closest size
    closest_waist = min(size_chart.keys(), key=lambda x: abs(x - waist))
    return size_chart[closest_waist]

def get_pant_size(measurements):
    """
    Convert body measurements to US pant size.
    
    Args:
        measurements (dict): Dictionary containing waist and hips measurements
    
    Returns:
        int: US pant size
    """
    if not all(key in measurements for key in ['waist', 'hips']):
        return None
        
    waist = measurements['waist']
    
    # Similar to dress size chart but specific for pants
    pant_chart = {
        24: 0,
        25: 2,
        26: 4,
        27.5: 6,
        29: 8,
        30.5: 10,
        32: 12,
        34: 14,
        36: 16,
        38: 18,
        40: 20
    }
    
    closest_waist = min(pant_chart.keys(), key=lambda x: abs(x - waist))
    return pant_chart[closest_waist]

def get_top_size(measurements):
    """
    Convert body measurements to US top size.
    
    Args:
        measurements (dict): Dictionary containing bust measurements
    
    Returns:
        str: US top size (XS, S, M, L, XL, etc.)
    """
    if 'bust' not in measurements:
        return None
        
    bust = measurements['bust']
    
    # Top size conversion chart
    size_chart = {
        32: 'XS',
        34: 'S',
        36: 'M',
        38: 'L',
        40: 'XL',
        42: '2XL',
        44: '3XL'
    }
    
    closest_bust = min(size_chart.keys(), key=lambda x: abs(x - bust))
    return size_chart[closest_bust]

def convert_shoe_size(us_size):
    """
    Convert US shoe size to European (French/Italian) and UK sizes.
    
    Args:
        us_size (float): US shoe size
    
    Returns:
        dict: Dictionary containing equivalent sizes
    """
    # Conversion formulas
    eu_size = round((us_size + 31.5), 0)  # French/Italian
    uk_size = round((us_size - 1), 0)
    
    return {
        'US': us_size,
        'EU': eu_size,
        'UK': uk_size
    }

def convert_clothing_size(size, size_type='dress'):
    """
    Convert US clothing sizes to French, Italian, and UK sizes.
    
    Args:
        size: US size to convert
        size_type (str): Type of clothing ('dress', 'top', or 'pant')
    
    Returns:
        dict: Dictionary containing equivalent sizes
    """
    # International size conversion charts
    dress_conversion = {
        0: {'FR': 32, 'IT': 36, 'UK': 4},
        2: {'FR': 34, 'IT': 38, 'UK': 6},
        4: {'FR': 36, 'IT': 40, 'UK': 8},
        6: {'FR': 38, 'IT': 42, 'UK': 10},
        8: {'FR': 40, 'IT': 44, 'UK': 12},
        10: {'FR': 42, 'IT': 46, 'UK': 14},
        12: {'FR': 44, 'IT': 48, 'UK': 16},
        14: {'FR': 46, 'IT': 50, 'UK': 18},
        16: {'FR': 48, 'IT': 52, 'UK': 20}
    }
    
    # For tops, convert letter sizes to numerical before conversion
    top_to_numerical = {
        'XS': 2,
        'S': 4,
        'M': 8,
        'L': 12,
        'XL': 16,
        '2XL': 18,
        '3XL': 20
    }
    
    if size_type == 'top' and isinstance(size, str):
        size = top_to_numerical.get(size, 8)  # Default to 8 if size not found
    
    # Use dress conversion chart for all types as base conversion
    if size in dress_conversion:
        return {
            'US': size,
            'FR': dress_conversion[size]['FR'],
            'IT': dress_conversion[size]['IT'],
            'UK': dress_conversion[size]['UK']
        }
    return None
