import streamlit as st
import pandas as pd
import os
#from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
#from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

# # اسم ملف الاكسل
# DATA_FILE = "data.xlsx"

# # --- إعداد الصفحة ---
# st.set_page_config(page_title="Location Portal", layout="wide")

# # --- Sidebar للتنقل بين الصفحات ---
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Add Location", "View Locations"])

# # --- دالة لحفظ البيانات في Excel ---
# def save_to_excel(new_data):
#     if os.path.exists(DATA_FILE):
#         df = pd.read_excel(DATA_FILE)
#         df = pd.concat([df, new_data], ignore_index=True)
#     else:
#         df = new_data
#     df.to_excel(DATA_FILE, index=False)

# # --- صفحة إضافة البيانات ---
# if page == "Add Location":
#     st.title("📝 Add New Location")

#     with st.form("location_form"):
#         area = st.text_input("Area")
#         city = st.text_input("City")
#         street = st.text_input("Street / Location Address")
#         latitude = st.number_input("Latitude", format="%.6f")
#         longitude = st.number_input("Longitude", format="%.6f")
#         nearby_pharmacies = st.text_area("Nearby Pharmacies (comma separated)")
#         other_locations = st.text_area("Other Nearby Locations")
#         population = st.number_input("Population", min_value=0)
#         competitor = st.number_input("Competitor Count", min_value=0)
#         accessibility = st.selectbox("Accessibility", ["Low", "Medium", "High"])
#         rent = st.number_input("Rent Cost", min_value=0)
#         score = st.number_input("Score", min_value=0)
#         recommendation = st.text_area("Recommendation / Notes")

#         submitted = st.form_submit_button("Save Location")
#         if submitted:
#             new_row = pd.DataFrame({
#                 "Area": [area],
#                 "City": [city],
#                 "Street": [street],
#                 "Latitude": [latitude],
#                 "Longitude": [longitude],
#                 "Nearby Pharmacies": [nearby_pharmacies],
#                 "Other Locations": [other_locations],
#                 "Population": [population],
#                 "Competitor": [competitor],
#                 "Accessibility": [accessibility],
#                 "Rent": [rent],
#                 "Score": [score],
#                 "Recommendation": [recommendation]
#             })
#             save_to_excel(new_row)
#             st.success("✅ Location saved successfully!")

# # --- صفحة عرض البيانات ---
# elif page == "View Locations":
#     st.title("📊 View All Locations")
#     if os.path.exists(DATA_FILE):
#         df = pd.read_excel(DATA_FILE)
#         st.dataframe(df)

#         st.markdown("### Filters")
#         area_filter = st.multiselect("Filter by Area", options=df["Area"].unique())
#         city_filter = st.multiselect("Filter by City", options=df["City"].unique())

#         filtered = df
#         if area_filter:
#             filtered = filtered[filtered["Area"].isin(area_filter)]
#         if city_filter:
#             filtered = filtered[filtered["City"].isin(city_filter)]

#         st.dataframe(filtered)

#         # عرض خريطة مع المواقع
#         st.markdown("### 🗺️ Location Map")
#         if not filtered.empty:
#             st.map(filtered[["Latitude", "Longitude"]])
#     else:
#         st.info("No data yet. Add locations in the 'Add Location' page.")



import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Location Evaluation Portal", layout="wide")

st.title("📍 New Location Evaluation")

# --- تحديد ملف البيانات ---
DATA_FILE = "data.xlsx"

# --- Sidebar للتنقل بين صفحات Add و View ---
page = st.sidebar.selectbox("Choose Page", ["Add Location", "View Locations"])

if page == "Add Location":
    st.header("Add New Location")
    area=['north','asir','south','middle']
    city=['Riyadh','Jeddah','Mecca','Medina','Dammam','Khobar','Tabuk','Abha','Buraidah','Hail','Najran','Jizan','Al‑Baha','Al‑Jouf','Arar']
    # --- Location Details ---
    pharmacy_type=st.selectbox('pharmacy_type',options=['Destination','Convenience'])
    st.subheader("1️⃣ Location")
    area = st.selectbox('choose area',options=area)
    city = st.selectbox('choose city',options=city)
    street = st.text_input("Street")
    #google_map_url = st.text_input("google_map_url")
    url=st.text_input('google maps url')
    #population_denisity = st.number_input("population",format="%.6f" )
    neighborhood_entrance=st.selectbox('neighborhood entrance',list(range(1,11)))
    accessibility = st.selectbox("Accessibility (1-10)", list(range(1,11)))
    visibility = st.selectbox("Visibility (1-10)", list(range(1,11)))
    nearby_landmarks = st.selectbox("Nearby Landmarks (1-10)", list(range(1,11)))
    

    # --- Traffic ---
    st.subheader("2️⃣ Traffic")
    main_traffic=st.selectbox('main traffic',options=['vehicle','pedestrian'])
    #vehicle_traffic = st.selectbox("Vehicle Traffic (1-10)", list(range(1,11)))
    st.markdown("**Vehicle Traffic **")
    cols = st.columns(5)  # نعمل 5 خانات جنب بعض
    traffic_inputs = []

    for i in range(5):
        with cols[i]:
            val = st.number_input(f"{i+1}", step=0.1, key=f"traffic_{i}")
            traffic_inputs.append(val)

# نحسب المتوسط
    if len(traffic_inputs) > 0:
        vehicle_traffic = sum(traffic_inputs) / len(traffic_inputs)
    else:
        vehicle_traffic = 0
        pedestrian_traffic = st.selectbox("Pedestrian Traffic (1-10)", list(range(1,11)))
    parking_availability = st.selectbox("Parking Availability (1-10)", list(range(1,11)))

    # --- Target Customer ---
    st.subheader("3️⃣ Target Customer")
    population_size = st.number_input("Population Size")
    income = st.selectbox("Income Level (1-10)", list(range(1,11)))
    market_share=.30
    average_sales_per_customer_month=st.number_input('average_sales_per_customer')
    estimated_sales=(average_sales_per_customer_month/30)*(population_size*market_share)

    # --- Competition ---
    st.subheader("4️⃣ Competition")
    #st.write('sales type mix depth')
    
    #sales_type_mix_depth = st.number_input("Number of Competitors", min_value=0, step=1)
    location_from_competitor = st.selectbox("location from competitor",options=['before','after'])
    st.write('competitor_type (score from 12)')
    col1,col2,col3,col4 =st.columns(4)
    score_map_col1 = {'type1': 2, 'ins1': 1, 'was1': 1}
    score_map_col2 = {'type2': 1, 'ins2': 1, 'was2': 1}
    score_map_col3 = {'type3': 2, 'ins3': 1, 'was3': 1}
    score_map_col4 = {'type4': 1}
    with col1:
        type1=st.radio('chain',['yes','no'],index=1,horizontal=True)
        ins1=st.radio('insurance(chain)',['yes','no'],index=1,horizontal=True)
        was1=st.radio('wasfaty(chain)',['yes','no'],index=1,horizontal=True)

    with col2:
        type2=st.radio('independent',['yes','no'],index=1,horizontal=True)
        ins2=st.radio('insurance(indep)',['yes','no'],index=1,horizontal=True)
        was2=st.radio('wasfaty(indep)',['yes','no'],index=1,horizontal=True)
    with col3:
        type3=st.radio('outlet',['yes','no'],index=1,horizontal=True)
        ins3=st.radio('insurance(outlet)',['yes','no'],index=1,horizontal=True)
        was3=st.radio('wasfaty(outlet)',['yes','no'],index=1,horizontal=True)
    with col4:
        type4=st.radio('milk&diaper shop',['yes','no'],index=1,horizontal=True)
    def get_score(val, score):
        return score if val == 'yes' else 0

    competition_score = (
    get_score(type1, score_map_col1['type1']) +
    get_score(ins1, score_map_col1['ins1']) +
    get_score(was1, score_map_col1['was1']) +
    
    get_score(type2, score_map_col2['type2']) +
    get_score(ins2, score_map_col2['ins2']) +
    get_score(was2, score_map_col2['was2']) +
    
    get_score(type3, score_map_col3['type3']) +
    get_score(ins3, score_map_col3['ins3']) +
    get_score(was3, score_map_col3['was3']) +
    
    get_score(type4, score_map_col4['type4'])
)
    
    # --- Building Infrastructure ---
    st.subheader("5️⃣ Building Infrastructure")
    building_size = st.number_input("Building Size (sqm)", min_value=0)
    building_condition = st.selectbox("Building Condition (1-10)", list(range(1,11)))
    shape=st.selectbox('shape',options=['corner','inline','end-cap','flag_shape','irregular','stand-alone','drive-thru'])
    parking_availability
    rent=st.number_input('rent')

    st.subheader('Added value')
    future_growth_potential=st.selectbox('future growth potential (منطقه نمو سكاني او تجاري)',list(range(1,11)))
    nearby_hospital=st.selectbox('nearby hospital',list(range(1,11)))
    nearby_united=st.radio('is nearby united pharmacy ?',['yes','no'])
    nearby_united_apt_no = ""
    nearby_united_transaction_no = ""
    if nearby_united=='yes':
        nearby_united_transaction_no=st.number_input('nearby_united_transaction_no')
        nearby_united_apt_no=st.number_input('nearby_united_apt_no')

    # --- Save Button ---
    if st.button("💾 Save Location"):
        new_data = {
            "Area": area,
            "City": city,
            "Street": street,
            'url':url,
            'pharmacy_type':pharmacy_type,

            "Accessibility": accessibility,
            "Visibility": visibility,
            "Nearby Landmarks": nearby_landmarks,

            "Vehicle Traffic": vehicle_traffic,
            "Parking Availability": parking_availability,

            "Population Size": population_size,
            "Income": income,
            'estimated sales':estimated_sales,

            
            "location_from_competitor": location_from_competitor,
            'competition_score':competition_score,

            "Building Size": building_size,
            "Building Condition": building_condition,
            'shape':shape,
            'rent':rent,

            'future growth potential':future_growth_potential,
            'nearby hospital':nearby_hospital,
            'nearby_united_transaction_no':nearby_united_transaction_no,
            'nearby_united_apt_no':nearby_united_apt_no
        }

        if os.path.exists(DATA_FILE):
            df = pd.read_excel(DATA_FILE)
            #df = df.append(new_data, ignore_index=True)
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

        else:
            df = pd.DataFrame([new_data])
        
        df.to_excel(DATA_FILE, index=False)
        st.success("✅ Location saved successfully!")

elif page == "View Locations":

    st.header("📊 View All Locations")
    # if os.path.exists(DATA_FILE):
    #     df = pd.read_excel(DATA_FILE)
    #     st.dataframe(df)
    
    # else:
    #     st.warning("No data found. Please add locations first.")
    #df.columns
    area_list = ['north','asir','south','middle']
    city_list = ['Riyadh','Jeddah','Mecca','Medina','Dammam','Khobar','Tabuk','Abha','Buraidah',
             'Hail','Najran','Jizan','Al‑Baha','Al‑Jouf','Arar']

    st.sidebar.title("Filters")
    selected_area = st.sidebar.selectbox("Select Area", ["All"] + area_list)
    selected_city = st.sidebar.selectbox("Select City", ["All"] + city_list)
    st.set_page_config(page_title="Location Evaluation Portal", layout="wide")
    if os.path.exists(DATA_FILE):
        df = pd.read_excel(DATA_FILE)

        filtered_df = df.copy()

    # فلترة حسب Area
        if selected_area != "All":
            filtered_df = filtered_df[filtered_df['Area'] == selected_area]

    # فلترة حسب City
        if selected_city != "All":
            filtered_df = filtered_df[filtered_df['City'] == selected_city]

        if filtered_df.empty:
            st.warning('⚠️ No records found for the selected filters.')
        else:
            st.dataframe(filtered_df)

        st.subheader("Filter by Index")
        index_list = df.index.tolist()
        selected_index = st.selectbox("Select Index",  index_list)
        if selected_index in index_list:
            filtered_df = df.loc[int(selected_index)]
        st.write("### Row Details")
        for col, val in filtered_df.items():
            st.write(f"**{col}:** {val}")
        st.subheader('CTQS')
        ctqs=filtered_df[['Accessibility','Visibility','Vehicle Traffic','Population Size']]
        ctqs
        
        for col_name in ["Merchandising and Layout Approval", "Finance Approval", "Operation Approval"]:
            if col_name not in df.columns:
                df[col_name] = ""

        # --- Approval Buttons ---
        col1, col2, col3 = st.columns(3)

        #with col1:
            #if st.button("✅ Merchandising Approval", key=f"merch_{selected_index}"):
                #df.at[selected_index, "Merchandising and Layout Approval"] = "Approved"
                #df.to_excel(DATA_FILE, index=False)
                #st.success("Merchandising & Layout Approved!")

        # with col2:
        #     if st.button("💰 Finance Approval", key=f"finance_{selected_index}"):
        #         df.at[selected_index, "Finance Approval"] = "Approved"
        #         df.to_excel(DATA_FILE, index=False)
        #         st.success("Finance Approved!")

        # with col3:
        #     if st.button("⚙️ Operation Approval", key=f"operation_{selected_index}"):
        #         df.at[selected_index, "Operation Approval"] = "Approved"
        #         df.to_excel(DATA_FILE, index=False)
        #         st.success("Operation Approved!")

        st.subheader("Choose Department View")
        col1,col2,col3=st.columns(3)
        if 'page' not in st.session_state:
            st.session_state.page = "View Locations"
        

        with col1:
            if st.button("📦 Merchandising"):
                st.session_state.page = "merchandising"

        with col2:
            if st.button("💰 Finance"):
                st.session_state.page = "finance"

        with col3:
            if st.button("⚙️ Operation"):
                st.session_state.page = "operation"
        if st.session_state.page == "View Locations":
            st.write("Select a department above to view its points.")

        elif st.session_state.page == "merchandising":
            st.header("📦 Merchandising Points")
            
        # اعرض فقط الأعمدة المتعلقة بالmerchandising
            merch_cols = filtered_df[["Area","City","Street","Accessibility","Visibility","Nearby Landmarks","competition_score"]]
            merch_cols
            if st.button("✅ Merchandising Approval", key=f"merch_{selected_index}"):
                df.at[selected_index, "Merchandising and Layout Approval"] = "Approved"
                df.to_excel(DATA_FILE, index=False)
                st.success("Merchandising & Layout Approved!")
        elif st.session_state.page=='finance':
            st.header('finance points')
            finance_col=filtered_df[['estimated sales','rent']]
            finance_col
            if st.button("💰 Finance Approval", key=f"finance_{selected_index}"):
                df.at[selected_index, "Finance Approval"] = "Approved"
                df.to_excel(DATA_FILE, index=False)
                st.success("Finance Approved!")
        elif st.session_state.page=='operation':
            st.header('operation points')
            operation_col=filtered_df
            operation_col
            if st.button("⚙️ Operation Approval", key=f"operation_{selected_index}"):
                 df.at[selected_index, "Operation Approval"] = "Approved"
                 df.to_excel(DATA_FILE, index=False)
                 st.success("Operation Approved!")
        
    
    else:
        st.warning("No data found. Please add locations first.")
    calc_df=filtered_df.copy()
    
    calc_df['location summary']=((calc_df['Accessibility']+calc_df['Visibility']+calc_df['Nearby Landmarks'])/3)*.25
    calc_df['traffic summary']=((calc_df['Vehicle Traffic']+calc_df['Parking Availability'])/2)*.2
    def rank_population(pop):
        if pop >= 100000:
            return 10
        elif pop >= 90000:
            return 9
        elif pop >= 80000:
            return 8
        elif pop >= 70000:
            return 7
        elif pop >= 60000:
            return 6
        elif pop >= 50000:
            return 5
        elif pop >= 40000:
            return 4
        elif pop >= 30000:
            return 3
        elif pop >= 20000:
            return 2
        else:
            return 1

    

# تأكد إنها DataFrame مش Series
    if isinstance(calc_df, pd.Series):
        calc_df = calc_df.to_frame().T

    

    calc_df['population rank'] = calc_df['Population Size'].apply(rank_population)
    

    calc_df['population summary']=((calc_df['population rank']+calc_df['Income'])/2)*.25
    calc_df['competion summary']=calc_df['competition_score']*-.15
    def rent_score(n):
        if n['rent'] <= .05*n['estimated sales']:
            return 10
        elif n['rent'] <= .08*n['estimated sales']:
            return 7
        elif n['rent'] <= .10*n['estimated sales']:
            return 5
        elif n['rent'] < .15*n['estimated sales']:
            return 3
        else:
            return 1
    calc_df['rent rank'] = calc_df.apply(rent_score, axis=1)

    #calc_df['rent rank']=calc_df['rent'].apply(rent_score)
    calc_df['infrastructure summary']=calc_df['rent rank']*.1
    
    calc_df['total score']=(calc_df['location summary']+calc_df['traffic summary']+calc_df['population summary']+calc_df['competion summary']+calc_df['infrastructure summary']).clip(upper=10)
    st.subheader(f"TOTAL SCORE IS : {calc_df['total score'].values}")


    
    

