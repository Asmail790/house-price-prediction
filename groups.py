DESC_KEY = "desc"
VALUES_DESC_KEY = "values"
LABEL_KEY = "label"
MIN = "min"
MAX = "max"
FIELD_TYPE = "type" 

DATAFIELDS_DESC = {
    "MSSubClass": {
        DESC_KEY: "Identifies the type of dwelling involved in the sale.",
        VALUES_DESC_KEY: {
            20: "1-STORY 1946 & NEWER ALL STYLES",
            30: "1-STORY 1945 & OLDER",
            40: "1-STORY W/FINISHED ATTIC ALL AGES",
            45: "1-1/2 STORY - UNFINISHED ALL AGES",
            50: "1-1/2 STORY FINISHED ALL AGES",
            60: "2-STORY 1946 & NEWER",
            70: "2-STORY 1945 & OLDER",
            75: "2-1/2 STORY ALL AGES",
            80: "SPLIT OR MULTI-LEVEL",
            85: "SPLIT FOYER",
            90: "DUPLEX - ALL STYLES AND AGES",
            120: "1-STORY PUD (Planned Unit Development) - 1946 & NEWER",
            150: "1-1/2 STORY PUD - ALL AGES",
            160: "2-STORY PUD - 1946 & NEWER",
            180: "PUD - MULTILEVEL - INCL SPLIT LEV/FOYER",
            190: "2 FAMILY CONVERSION - ALL STYLES AND AGES",
        },
        "MSZoning": {
            DESC_KEY: "Identifies the general zoning classification of the sale.",
            VALUES_DESC_KEY: {
                "A", "Agriculture"
                "C", "Commercial"
                "FV", "Floating Village Residential"
                "I", "Industrial"
                "RH", "Residential High Density"
                "RL", "Residential Low Density"
                "RP", "Residential Low Density Park"
                "RM", "Residential Medium Density"
            }
        },
        "LotFrontage": {
            DESC_KEY: "Linear feet of street connected to property"
        },
        "LotArea": {
            DESC_KEY: "Lot size in square feet"
        },
        "Street": {
            DESC_KEY: "Type of road access to property",
            VALUES_DESC_KEY: {
                "Grvl": "Gravel",
                "Pave": "Paved",
            }
        },
        "Alley": {
            DESC_KEY: "Type of alley access to property",
            VALUES_DESC_KEY: {
                "Grvl": "Gravel",
                "Pave": "Paved",
                "NA": "No alley access",
            }
        },
        "LotShape": {
            DESC_KEY: "General shape of property",
            VALUES_DESC_KEY: {
                "Reg": "Regular",
                "IR1": "Slightly irregular",
                "IR2": "Moderately Irregular",
                "IR3": "Irregular",
            }
        },
        "LandContour": {
            DESC_KEY: "Flatness of the property",
            VALUES_DESC_KEY: {
                "Lvl": "Near Flat/Level",
                "Bnk": "Banked - Quick and significant rise from street grade to building",
                "HLS": "Hillside - Significant slope from side to side",
                "Low": "Depression",
            }
        },
        "Utilities": {
            DESC_KEY: "Type of utilities available",
            VALUES_DESC_KEY: {
                "AllPub": "All public Utilities (E,G,W,& S)",
                "NoSewr": "Electricity, Gas, and Water (Septic Tank)",
                "NoSeWa": "Electricity and Gas Only",
                "ELO": "Electricity only",
            }
        },
        "LotConfig": {
            DESC_KEY: "Lot configuration",
            VALUES_DESC_KEY: {
                "Inside": "Inside lot",
                "Corner": "Corner lot",
                "CulDSac": "Cul-de-sac",
                "FR2": "Frontage on 2 sides of property",
                "FR3": "Frontage on 3 sides of property",
            }
        },
        "LandSlope": {
            DESC_KEY: "Slope of property",
            VALUES_DESC_KEY: {
                "Gtl": "Gentle slope",
                "Mod": "Moderate Slope",
                "Sev": "Severe Slope",
            }
        },
        "Neighborhood": {
            DESC_KEY: "Physical locations within Ames city limits",
            VALUES_DESC_KEY: {
                "Blueste": "Bluestem",
                "Blmngtn": "Bloomington Heights",
                "BrkSide": "Brookside",
                "BrDale": "Briardale",
                "ClearCr": "Clear Creek",
                "CollgCr": "College Creek",
                "Crawfor": "Crawford",
                "Edwards": "Edwards",
                "Gilbert": "Gilbert",
                "IDOTRR": "Iowa DOT and Rail Road",
                "MeadowV": "Meadow Village",
                "Mitchel": "Mitchell",
                "Names": "North Ames",
                "NoRidge": "Northridge",
                "NPkVill": "Northpark Villa",
                "NridgHt": "Northridge Heights",
                "NWAmes": "Northwest Ames",
                "OldTown": "Old Town",
                "SWISU": "South & West of Iowa State University",
                "Sawyer": "Sawyer",
                "SawyerW": "Sawyer West",
                "Somerst": "Somerset",
                "StoneBr": "Stone Brook",
                "Timber": "Timberland",
                "Veenker": "Veenker",
            }
        },
        "Condition1": {
            DESC_KEY: "Proximity to various conditions",
            VALUES_DESC_KEY: {
                "Artery": "Adjacent to arterial street",
                "Feedr": "Adjacent to feeder street",
                "Norm": "Normal",
                "RRNn": "Within 200' of North-South Railroad",
                "RRAn": "Adjacent to North-South Railroad",
                "PosN": "Near positive off-site feature--park, greenbelt, etc.",
                "PosA": "Adjacent to postive off-site feature",
                "RRNe": "Within 200' of East-West Railroad",
                "RRAe": "Adjacent to East-West Railroad",
            }
        },
        "Condition2": {
            DESC_KEY: "Proximity to various conditions (if more than one is present)",
            VALUES_DESC_KEY: {
                "Artery": "Adjacent to arterial street",
                "Feedr": "Adjacent to feeder street",
                "Norm": "Normal",
                "RRNn": "Within 200' of North-South Railroad",
                "RRAn": "Adjacent to North-South Railroad",
                "PosN": "Near positive off-site feature--park, greenbelt, etc.",
                "PosA": "Adjacent to postive off-site feature",
                "RRNe": "Within 200' of East-West Railroad",
                "RRAe": "Adjacent to East-West Railroad",
            }
        },
        "BldgType": {
            DESC_KEY: "Type of dwelling",
            VALUES_DESC_KEY: {
                "1Fam": "Single-family Detached",
                "2FmCon": "Two-family Conversion; originally built as one-family dwelling",
                "Duplx": "Duplex",
                "TwnhsE": "Townhouse End Unit",
                "TwnhsI": "Townhouse Inside Unit",
            }
        },
        "HouseStyle": {
            "Style of dwelling"

            "1Story": "One story",
            "1.5Fin": "One and one-half story: 2nd level finished",
            "1.5Unf": "One and one-half story: 2nd level unfinished",
            "2Story": "Two story",
            "2.5Fin": "Two and one-half story: 2nd level finished",
            "2.5Unf": "Two and one-half story: 2nd level unfinished",
            "SFoyer": "Split Foyer",
            "SLvl": "Split Level",
        }
    },
    "OverallQual": {
        DESC_KEY: "Rates the overall material and finish of the house",
        VALUES_DESC_KEY: {
            "10": "Very Excellent",
            "9": "Excellent",
            "8": "Very Good",
            "7": "Good",
            "6": "Above Average",
            "5": "Average",
            "4": "Below Average",
            "3": "Fair",
            "2": "Poor",
            "1": "Very Poor",
        }
    },
    "OverallCond": {
        DESC_KEY: "Rates the overall condition of the house",
        VALUES_DESC_KEY: {
            "10": "Very Excellent",
            "9": "Excellent",
            "8": "Very Good",
            "7": "Good",
            "6": "Above Average",
            "5": "Average",
            "4": "Below Average",
            "3": "Fair",
            "2": "Poor",
            "1": "Very Poor",
        }
    },
    "YearBuilt": {
        DESC_KEY: "Original construction date",
        FIELD_TYPE:"number",
        MIN:1900
    },
    "YearRemodAdd": {
        DESC_KEY: "Remodel date (same as construction date if no remodeling or additions)",
        VALUES_DESC_KEY: {
        }
    },
    "RoofStyle": {
        DESC_KEY: "Type of roof",
        VALUES_DESC_KEY: {

            "Flat": "Flat",
            "Gable": "Gable",
            "Gambrel": "Gabrel (Barn)",
            "Hip": "Hip",
            "Mansard": "Mansard",
            "Shed": "Shed",
        }
    },
    "RoofMatl": {
        DESC_KEY: "Roof material",
        VALUES_DESC_KEY: {

            "ClyTile": "Clay or Tile",
            "CompShg": "Standard (Composite) Shingle",
            "Membran": "Membrane",
            "Metal": "Metal",
            "Roll": "Roll",
            "Tar&Grv": "Gravel & Tar",
            "WdShake": "Wood Shakes",
            "WdShngl": "Wood Shingles",
        }
    },
    "Exterior1st": {
        DESC_KEY: "Exterior covering on house",
        VALUES_DESC_KEY: {

            "AsbShng": "Asbestos Shingles",
            "AsphShn": "Asphalt Shingles",
            "BrkComm": "Brick Common",
            "BrkFace": "Brick Face",
            "CBlock": "Cinder Block",
            "CemntBd": "Cement Board",
            "HdBoard": "Hard Board",
            "ImStucc": "Imitation Stucco",
            "MetalSd": "Metal Siding",
            "Other": "Other",
            "Plywood": "Plywood",
            "PreCast": "PreCast",
            "Stone": "Stone",
            "Stucco": "Stucco",
            "VinylSd": "Vinyl Siding",
            "Wd Sdng": "Wood Siding",
            "WdShing": "Wood Shingles",
        }
    },
    "Exterior2nd": {
        DESC_KEY: "Exterior covering on house (if more than one material)",
        VALUES_DESC_KEY: {

            "AsbShng": "Asbestos Shingles",
            "AsphShn": "Asphalt Shingles",
            "BrkComm": "Brick Common",
            "BrkFace": "Brick Face",
            "CBlock": "Cinder Block",
            "CemntBd": "Cement Board",
            "HdBoard": "Hard Board",
            "ImStucc": "Imitation Stucco",
            "MetalSd": "Metal Siding",
            "Other": "Other",
            "Plywood": "Plywood",
            "PreCast": "PreCast",
            "Stone": "Stone",
            "Stucco": "Stucco",
            "VinylSd": "Vinyl Siding",
            "Wd": "Sdng	Wood Siding",
            "WdShing": "Wood Shingles",
        }
    },
    "MasVnrType": {
        DESC_KEY: "Masonry veneer type",
        VALUES_DESC_KEY: {

            "BrkCmn": "Brick Common",
            "BrkFace": "Brick Face",
            "CBlock": "Cinder Block",
            "None": "None",
            "Stone": "Stone",
        }
    },
    "MasVnrArea": {
        DESC_KEY: "Masonry veneer area in square feet"
    },
    "ExterQual": {
        DESC_KEY: "Evaluates the quality of the material on the exterior",
        VALUES_DESC_KEY: {
            "Ex": "Excellent",
            "Gd": "Good",
            "TA": "Average/Typical",
            "Fa": "Fair",
            "Po": "Poor",
        }
    },
    "ExterCond": {
        DESC_KEY: "Evaluates the present condition of the material on the exterior",
        VALUES_DESC_KEY: {
            "Ex": "Excellent",
            "Gd": "Good",
            "TA": "Average/Typical",
            "Fa": "Fair",
            "Po": "Poor",
        }
    },
    "Foundation": {
        DESC_KEY: "Type of foundation",
        VALUES_DESC_KEY: {
            "BrkTil": "Brick & Tile",
            "CBlock": "Cinder Block",
            "PConc": "Poured Contrete",
            "Slab": "Slab",
            "Stone": "Stone",
            "Wood": "Wood",
        }
    },
    "BsmtQual": {
        DESC_KEY: "Evaluates the height of the basement",
        FIELD_TYPE:"dropdown",
        VALUES_DESC_KEY: {
            "Ex": "Excellent (100+ inches)",
            "Gd": "Good (90-99 inches)",
            "TA": "Typical (80-89 inches)",
            "Fa": "Fair (70-79 inches)",
            "Po": "Poor (<70 inches",
            "NA": "No Basement",
        }
    },
    "BsmtCond": {
        DESC_KEY: "Evaluates the general condition of the basement",
        VALUES_DESC_KEY: {

            "Ex": "Excellent",
            "Gd": "Good",
            "TA": "Typical - slight dampness allowed",
            "Fa": "Fair - dampness or some cracking or settling",
            "Po": "Poor - Severe cracking, settling, or wetness",
            "NA": "No Basement",
        }
    },
    "BsmtExposure": {
        DESC_KEY: "Refers to walkout or garden level walls",
        VALUES_DESC_KEY: {

            "Gd": "Good Exposure",
            "Av": "Average Exposure (split levels or foyers typically score average or above)",
            "Mn": "Mimimum Exposure",
            "No": "No Exposure",
            "NA": "No Basement",
        }
    },
    "BsmtFinType1": {
        DESC_KEY: "Rating of basement finished area",
        VALUES_DESC_KEY: {
            "GLQ": "Good Living Quarters",
            "ALQ": "Average Living Quarters",
            "BLQ": "Below Average Living Quarters",
            "Rec": "Average Rec Room",
            "LwQ": "Low Quality",
            "Unf": "Unfinshed",
            "NA": "No Basement",
        }
    },
    "BsmtFinSF1": {
        DESC_KEY: "Type 1 finished square feet",
    },
    "BsmtFinType2": {
        DESC_KEY: "Rating of basement finished area (if multiple types)",
        VALUES_DESC_KEY: {

            "GLQ": "Good Living Quarters",
            "ALQ": "Average Living Quarters",
            "BLQ": "Below Average Living Quarters",
            "Rec": "Average Rec Room",
            "LwQ": "Low Quality",
            "Unf": "Unfinshed",
            "NA": "No Basement",
        }
    },
    "BsmtFinSF2": {
        DESC_KEY: "Type 2 finished square feet",
    },
    "BsmtUnfSF": {
        DESC_KEY: "Unfinished square feet of basement area",
    },

    "TotalBsmtSF": {
        DESC_KEY: "Size of basement area in square feet",
        FIELD_TYPE:"number",
        MIN:0
    },

    "Heating": {
        DESC_KEY: "Type of heating",
        VALUES_DESC_KEY: {
            "Floor": "Floor Furnace",
            "GasA": "Gas forced warm air furnace",
            "GasW": "Gas hot water or steam heat",
            "Grav": "Gravity furnace",
            "OthW": "Hot water or steam heat other than gas",
            "Wall": "Wall furnace",
        }
    },
    "HeatingQC": {
        DESC_KEY: "Heating quality and condition",
        VALUES_DESC_KEY: {

            "Ex": "Excellent",
            "Gd": "Good",
            "TA": "Average/Typical",
            "Fa": "Fair",
            "Po": "Poor",
        }
    },
    "CentralAir": {
        DESC_KEY: "Central air conditioning",
        VALUES_DESC_KEY: {

            "N": "No",
            "Y": "Yes",
        }
    },
    "Electrical": {
        DESC_KEY: "Electrical system",
        VALUES_DESC_KEY: {

            "SBrkr": "Standard Circuit Breakers & Romex",
            "FuseA": "Fuse Box over 60 AMP and all Romex wiring (Average)",
            "FuseF": "60 AMP Fuse Box and mostly Romex wiring (Fair)",
            "FuseP": "60 AMP Fuse Box and mostly knob & tube wiring (poor)",
            "Mix": "Mixed",
        }
    },
    "1stFlrSF": {
        DESC_KEY: "First Floor square feet"
    },
    "2ndFlrSF": {
        DESC_KEY: "Second floor square feet",
    },
    "LowQualFinSF": {
        DESC_KEY: "Low quality finished square feet (all floors)",
    },

    "GrLivArea": {
        DESC_KEY: "Size of above grade (ground) living area in square feet",
        FIELD_TYPE:"number",
        MIN:0
    },

    "BsmtFullBath": {
        DESC_KEY: "Basement full bathrooms",
    },

    "BsmtHalfBath": {
        DESC_KEY: "Basement half bathrooms",
    },

    "FullBath": {
        DESC_KEY: "Full bathrooms above grade",
    },

    "HalfBath": {
        DESC_KEY: "Half baths above grade",
    },

    "Bedroom": {
        DESC_KEY: "Bedrooms above grade (does NOT include basement bedrooms)",
    },

    "Kitchen": {
        DESC_KEY: "Kitchens above grade",
    },

    "KitchenQual": {
        DESC_KEY: "Kitchen quality",
        VALUES_DESC_KEY: {
            "Ex": "Excellent",
            "Gd": "Good",
            "TA": "Typical/Average",
            "Fa": "Fair",
            "Po": "Poor",
        }
    },
    "TotRmsAbvGrd": {
        DESC_KEY: "Total rooms above grade (does not include bathrooms)",
        FIELD_TYPE:"number",
        MAX:14,
        MIN:1
    },
    "Functional": {
        DESC_KEY: "Home functionality (Assume typical unless deductions are warranted)",
        VALUES_DESC_KEY: {

            "Typ": "Typical Functionality",
            "Min1": "Minor Deductions 1",
            "Min2": "Minor Deductions 2",
            "Mod": "Moderate Deductions",
            "Maj1": "Major Deductions 1",
            "Maj2": "Major Deductions 2",
            "Sev": "Severely Damaged",
            "Sal": "Salvage only",
        },
    },
    "Fireplaces": {
        DESC_KEY: "Number of fireplaces",
    },

    "FireplaceQu": {
        DESC_KEY: "Fireplace quality",
        VALUES_DESC_KEY: {

            "Ex": "Excellent - Exceptional Masonry Fireplace",
            "Gd": "Good - Masonry Fireplace in main level",
            "TA": "Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement",
            "Fa": "Fair - Prefabricated Fireplace in basement",
            "Po": "Poor - Ben Franklin Stove",
            "NA": "No Fireplace",
        }
    },
    "GarageType": {
        DESC_KEY: "Garage location",
        VALUES_DESC_KEY: {
            "2Types": "More than one type of garage",
            "Attchd": "Attached to home",
            "Basment": "Basement Garage",
            "BuiltIn": "Built-In (Garage part of house - typically has room above garage)",
            "CarPort": "Car Port",
            "Detchd": "Detached from home",
            "NA": "No Garage",
        }
    },
    "GarageYrBlt": {
        DESC_KEY: "Year garage was built"
    },
    "GarageFinish": {
        DESC_KEY: "Interior finish of the garage",
        VALUES_DESC_KEY: {

            "Fin": "Finished",
            "RFn": "Rough Finished",
            "Unf": "Unfinished",
            "NA": "No Garage",
        }
    },
    "GarageCars": {
        DESC_KEY: "Size of garage in car capacity",
    },

    "GarageArea": {
        DESC_KEY: "Size of garage in square feet",
        FIELD_TYPE:"number",
        MIN:0
    },

    "GarageQual": {
        DESC_KEY: "Garage quality",
        VALUES_DESC_KEY: {

            "Ex": "Excellent",
            "Gd": "Good",
            "TA": "Typical/Average",
            "Fa": "Fair",
            "Po": "Poor",
            "NA": "No Garage",
        }
    },
    "GarageCond": {
        DESC_KEY: "Garage condition",
        VALUES_DESC_KEY: {

            "Ex": "Excellent",
            "Gd": "Good",
            "TA": "Typical/Average",
            "Fa": "Fair",
            "Po": "Poor",
            "NA": "No Garage",
        }
    },
    "PavedDrive": {
        DESC_KEY: "Paved driveway",
        VALUES_DESC_KEY: {

            "Y": "Paved",
            "P": "Partial Pavement",
            "N": "Dirt/Gravel",
        }
    },
    "WoodDeckSF": {
        DESC_KEY: "Wood deck area in square feet",
    },

    "OpenPorchSF": {
        DESC_KEY: "Open porch area in square feet",
    },

    "EnclosedPorch": {
        DESC_KEY: "Enclosed porch area in square feet",
    },

    "3SsnPorch": {
        DESC_KEY: "Three season porch area in square feet",
    },

    "ScreenPorch": {
        DESC_KEY: "Screen porch area in square feet",
    },

    "PoolArea": {
        DESC_KEY: "Pool area in square feet",
    },

    "PoolQC": {
        DESC_KEY: "Pool quality",
        VALUES_DESC_KEY: {
            "Ex": "Excellent",
            "Gd": "Good",
            "TA": "Average/Typical",
            "Fa": "Fair",
            "NA": "No Pool",
        }
    },
    "Fence": {
        DESC_KEY: "Fence quality",
        VALUES_DESC_KEY: {
            "GdPrv": "Good Privacy",
            "MnPrv": "Minimum Privacy",
            "GdWo": "Good Wood",
            "MnWw": "Minimum Wood/Wire",
            "NA": "No Fence",
        }
    },
    "MiscFeature": {
        DESC_KEY: "Miscellaneous feature not covered in other categories",
        VALUES_DESC_KEY: {
            "Elev": "Elevator",
            "Gar2": "2nd Garage (if not described in garage section)",
            "Othr": "Other",
            "Shed": "Shed (over 100 SF)",
            "TenC": "Tennis Court",
            "NA": "None",
        }
    },
    "MiscVal": {
        DESC_KEY: "Value of miscellaneous feature",
    },

    "MoSold": {
        DESC_KEY: "Month Sold (MM)",
    },
    "YrSold": {
        DESC_KEY: "Year Sold (YYYY)",
    },

    "SaleType": {
        DESC_KEY: "Type of sale",
        VALUES_DESC_KEY: {
            "WD": "Warranty Deed - Conventional",
            "CWD": "Warranty Deed - Cash",
            "VWD": "Warranty Deed - VA Loan",
            "New": "Home just constructed and sold",
            "COD": "Court Officer Deed/Estate",
            "Con": "Contract 15% Down payment regular terms",
            "ConLw": "Contract Low Down payment and low interest",
            "ConLI": "Contract Low Interest",
            "ConLD": "Contract Low Down",
            "Oth": "Other",
        }
    },
    "SaleCondition": {
        DESC_KEY: "Condition of sale",
        VALUES_DESC_KEY: {
            "Normal": "Normal Sale",
            "Abnorml": "Abnormal Sale -  trade, foreclosure, short sale",
            "AdjLand": "Adjoining Land Purchase",
            "Alloca": "Allocation - two linked properties with separate deeds, typically condo with a garage unit",
            "Family": "Sale between family members",
            "Partial": "Home was not completed when last assessed (associated with New Homes)",
        }
    },

    "have_Fireplace": {
        DESC_KEY: "Have a fire place",
        FIELD_TYPE:"checkbox",
        VALUES_DESC_KEY:{
            "Yes":1,
            "No":0 
        }
     },
    "have_WoodDeck": {
        DESC_KEY: "Have a wood deck",
        FIELD_TYPE:"checkbox",
        VALUES_DESC_KEY:{
            "Yes":1,
            "No":0 
        }
    },
    "have_Porch": {
        DESC_KEY: "Have a porch",
        FIELD_TYPE:"checkbox",
        VALUES_DESC_KEY:{
            "Yes":1,
            "No":0 
        }
    },
    "have_Garage": {
        DESC_KEY: "Garage exist",
        FIELD_TYPE:"checkbox",
        VALUES_DESC_KEY:{
            "Yes":1,
            "No":0 
        }
    },
    "total_Bath": {
        DESC_KEY: "Total number of bathrooms",
        FIELD_TYPE:"number",
        MIN:1,
        MAX:10
    }
}