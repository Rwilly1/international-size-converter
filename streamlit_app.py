import streamlit as st
import pandas as pd
import base64
from size_converter import (
    get_dress_size,
    get_pant_size,
    get_top_size,
    convert_shoe_size,
    convert_clothing_size
)

# Configure page first
st.set_page_config(page_title="International Size Converter", layout="wide")

# Function to load and encode the GIF
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set background image
def set_background(gif_path):
    bin_str = get_base64_of_bin_file(gif_path)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/gif;base64,%s");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Set the background GIF
set_background('rainbow.gif')

# Custom CSS for styling
st.markdown("""
    <style>
    /* Apply American Typewriter font to everything */
    .stApp, .stApp * {
        font-family: 'American Typewriter', 'Courier New', monospace !important;
    }

    /* Add margins */
    .main > div:first-child {
        padding-left: 2in !important;
        padding-right: 2in !important;
    }

    /* Style for content boxes - only for elements with actual content */
    div[data-testid="stTable"]:not(:empty),
    div.stMarkdown:has(h1, h2, h3, p, ul, ol),
    div[data-testid="stHeader"]:not(:empty),
    div.stSlider,
    div[data-baseweb="notification"] {
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-radius: 0.5rem !important;
        padding: 1rem !important;
        margin-bottom: 1rem !important;
        border: 1px solid rgba(49, 51, 63, 0.2) !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1) !important;
        width: 100% !important;
        box-sizing: border-box !important;
    }

    /* Remove margin from empty elements */
    div.stMarkdown:empty,
    div[data-testid="stMarkdownContainer"]:empty {
        margin: 0 !important;
        padding: 0 !important;
        height: 0 !important;
    }

    /* Ensure sliders fit in boxes */
    .stSlider {
        width: 100% !important;
        padding: 1rem !important;
        box-sizing: border-box !important;
    }

    .stSlider > div {
        width: 100% !important;
    }

    /* Keep warning boxes distinct */
    div[data-baseweb="notification"] {
        margin: 1rem 0 !important;
    }

    /* Center the content in columns */
    div[data-testid="column"] {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        width: 100% !important;
    }

    /* Center header content */
    .stApp > header {
        text-align: center;
    }

    .stApp h1, .stApp h2, .stApp h3, 
    div[data-testid="stMarkdownContainer"] > * {
        text-align: center !important;
    }

    /* Make all text black with American Typewriter */
    div[data-testid="stMarkdownContainer"] > h1, 
    div[data-testid="stMarkdownContainer"] > h2, 
    div[data-testid="stMarkdownContainer"] > h3,
    .stMarkdown, 
    div[data-testid="stText"],
    div[data-testid="stTable"], 
    .stNumberInput label,
    div[data-testid="stMarkdownContainer"] p,
    .stMarkdown code,
    div[data-testid="stTable"] td,
    .stNumberInput div[data-baseweb="input"],
    .stSelectbox div[class*="data-testid"],
    button[kind="secondary"] {
        font-family: 'American Typewriter', 'Courier New', monospace !important;
        color: black !important;
        -webkit-text-fill-color: black !important;
        text-shadow: none;
    }

    /* Style slider thumb (circle) and active track to be black */
    .stSlider div[data-baseweb="slider"] div[role="slider"] {
        background-color: black !important;
        border-color: black !important;
    }

    .stSlider div[data-baseweb="slider"] div[class*="progressBar"] {
        background-color: black !important;
    }
    
    /* Make ALL slider text black and American Typewriter */
    .stSlider div[data-testid="stMarkdownContainer"] p,
    .stSlider div[data-baseweb="slider"] div,
    .stSlider div[data-baseweb="slider"] span,
    .stSlider div[data-baseweb="slider"] p,
    .stSlider div[data-baseweb="slider"] tooltip,
    .stSlider div[class*="ThumbValue"],
    .stSlider div[class*="ValueLabel"],
    .stSlider div[class*="Mark"],
    .stSlider label {
        font-family: 'American Typewriter', 'Courier New', monospace !important;
        color: black !important;
        -webkit-text-fill-color: black !important;
    }
    
    /* Ensure tooltip text is black and American Typewriter */
    div[role="tooltip"] {
        font-family: 'American Typewriter', 'Courier New', monospace !important;
        color: black !important;
        -webkit-text-fill-color: black !important;
    }
    
    /* Style tables with black outline and transparent background */
    div[data-testid="stTable"] table {
        border: 2px solid black !important;
        background: transparent !important;
    }

    div[data-testid="stTable"] th,
    div[data-testid="stTable"] td {
        border: 1px solid black !important;
        background: transparent !important;
    }

    /* Style number inputs with black outline */
    .stNumberInput div[data-baseweb="input"] {
        border: 2px solid black !important;
        background: transparent !important;
    }

    /* Ensure inputs are visible with transparent background */
    input, select, textarea {
        color: black !important;
        background: transparent !important;
        border: 1px solid black !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("International Size Conversions")

# Add helpful information at the top with centered text
st.markdown("""
<div style='text-align: center;'>
<h3>How to Use</h3>
1. Enter your measurements in inches in the left panel<br>
2. Your US sizes will be automatically calculated and displayed<br>
3. Scroll down to see international size conversions<br>
4. All conversions update in real-time as you adjust your measurements

<h3>Note</h3>
Sizes are approximate and may vary by brand and style. When in doubt, always refer to the specific brand's size chart.
</div>
<div style='margin-bottom: 0.5in;'></div>
""", unsafe_allow_html=True)

st.write("")

# Create two columns for the input form
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Enter Your Measurements")
    bust = st.slider("Bust (inches)", min_value=20.0, max_value=60.0, value=34.0, step=0.5)
    waist = st.slider("Waist (inches)", min_value=20.0, max_value=60.0, value=28.0, step=0.5)
    hips = st.slider("Hips (inches)", min_value=20.0, max_value=60.0, value=36.0, step=0.5)
    shoe_size = st.slider("US Shoe Size", min_value=4.0, max_value=16.0, value=8.0, step=0.5)

# Create measurements dictionary
measurements = {
    'bust': bust,
    'waist': waist,
    'hips': hips,
    'shoe_size': shoe_size
}

# Validate measurements
is_valid = True

if waist >= bust:
    st.warning("⚠️ Warning: Waist measurement cannot be larger than or equal to bust measurement")
    is_valid = False
elif waist >= hips:
    st.warning("⚠️ Warning: Waist measurement cannot be larger than or equal to hip measurement")
    is_valid = False
elif bust < waist - 15 or bust > waist + 15:
    st.warning("⚠️ Warning: The difference between bust and waist measurements seems unrealistic")
    is_valid = False
elif hips < waist - 15 or hips > waist + 15:
    st.warning("⚠️ Warning: The difference between hips and waist measurements seems unrealistic")
    is_valid = False

if is_valid:
    # Calculate sizes
    dress_size = get_dress_size(measurements)
    pant_size = get_pant_size(measurements)
    top_size = get_top_size(measurements)
    shoe_sizes = convert_shoe_size(measurements['shoe_size'])

    with col2:
        st.subheader("Your US Sizes")
        sizes_df = pd.DataFrame({
            'Category': ['Dress Size', 'Pant Size', 'Top Size'],
            'US Size': [f'{dress_size}', f'{pant_size}', f'{top_size}']
        })
        st.table(sizes_df)
        
        st.write("")  # Add some spacing
        
        # Add shoe size conversion here
        st.subheader("Shoe Size Conversion")
        shoe_df = pd.DataFrame({
            'Region': ['US', 'European (EU)', 'UK'],
            'Size': [
                shoe_sizes['US'],
                shoe_sizes['EU'],
                shoe_sizes['UK']
            ]
        })
        st.table(shoe_df)

    # Add some vertical spacing before international sizes
    st.write("")

    # Display international size conversions
    st.header("Clothing Size Conversions")
    
    # Create three columns for different size types
    col_dress, col_pant, col_top = st.columns(3)

    with col_dress:
        st.subheader("Dress Sizes")
        if dress_size:  # Only show if we have a valid dress size
            dress_conversions = convert_clothing_size(dress_size, 'dress')
            dress_df = pd.DataFrame({
                'Region': ['US', 'French (FR)', 'Italian (IT)', 'UK'],
                'Size': [
                    dress_conversions['US'],
                    dress_conversions['FR'],
                    dress_conversions['IT'],
                    dress_conversions['UK']
                ]
            })
            st.table(dress_df)

    with col_pant:
        st.subheader("Pant Sizes")
        if pant_size:  # Only show if we have a valid pant size
            pant_conversions = convert_clothing_size(pant_size, 'pant')
            pant_df = pd.DataFrame({
                'Region': ['US', 'French (FR)', 'Italian (IT)', 'UK'],
                'Size': [
                    pant_conversions['US'],
                    pant_conversions['FR'],
                    pant_conversions['IT'],
                    pant_conversions['UK']
                ]
            })
            st.table(pant_df)

    with col_top:
        st.subheader("Top Sizes")
        if top_size:  # Only show if we have a valid top size
            top_conversions = convert_clothing_size(top_size, 'top')
            top_df = pd.DataFrame({
                'Region': ['US', 'French (FR)', 'Italian (IT)', 'UK'],
                'Size': [
                    top_conversions['US'],
                    top_conversions['FR'],
                    top_conversions['IT'],
                    top_conversions['UK']
                ]
            })
            st.table(top_df)
