import streamlit as st
import pandas as pd
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="electronics_store",
)

cursor = db.cursor()

st.set_page_config(
    page_title="Components CRUD UI",
    layout="wide",
    page_icon="🔌",
)

st.title("Components CRUD UI")

st.markdown(
    """
    This is the CRUD UI for the components table.
"""
)

st.markdown(
    """
    ## Table of all components
"""
)

cursor.execute("SELECT * FROM components")
components = cursor.fetchall()

components_df = pd.DataFrame(
    components,
    columns=[
        "comp_id",
        "description",
        "part_no",
        "mf_id",
        "name",
        "lifecycle",
        "category",
        "datasheet",
        "rohs",
        "mount_type",
    ],
)

st.dataframe(components_df)

st.markdown(
    """
    ## Add a new component
"""
)

comp_id = st.number_input("Component ID", key="comp_id_add")
description = st.text_input("Description", key="description_add")
part_no = st.text_input("Part Number", key="part_no_add")
mf_id = st.text_input("Manufacturer ID", key="mf_id_add")
name = st.text_input("Name", key="name_add")
lifecycle = st.text_input("Lifecycle", key="lifecycle_add")
category = st.text_input("Category", key="category_add")
datasheet = st.text_input("Datasheet", key="datasheet_add")
rohs = st.text_input("RoHS", key="rohs_add")
mount_type = st.text_input("Mount Type", key="mount_type_add")

if st.button("Add"):
    cursor.execute(
        f"INSERT INTO components VALUES ({comp_id}, '{description}', '{part_no}', '{mf_id}', '{name}', '{lifecycle}', '{category}', '{datasheet}', '{rohs}', '{mount_type}')"
    )
    db.commit()
    st.success("Component added successfully")

st.markdown(
    """
    ## Update an existing component
"""
)

comp_id = st.number_input("Component ID", key="comp_id_update")
description = st.text_input("Description", key="description_update")
part_no = st.text_input("Part Number", key="part_no_update")
mf_id = st.text_input("Manufacturer ID", key="mf_id_update")
name = st.text_input("Name", key="name_update")
lifecycle = st.text_input("Lifecycle", key="lifecycle_update")
category = st.text_input("Category", key="category_update")
datasheet = st.text_input("Datasheet", key="datasheet_update")
rohs = st.text_input("RoHS", key="rohs_update")
mount_type = st.text_input("Mount Type", key="mount_type_update")

if st.button("Update"):
    cursor.execute(
        f"UPDATE components SET description='{description}', part_no='{part_no}', mf_id='{mf_id}', name='{name}', lifecycle='{lifecycle}', category='{category}', datasheet='{datasheet}', rohs='{rohs}', mount_type='{mount_type}' WHERE comp_id={comp_id}"
    )
    db.commit()
    st.success("Component updated successfully")

st.markdown(
    """
    ## Delete an existing component
"""
)

comp_id = st.number_input("Component ID", key="comp_id_delete")

if st.button("Delete"):
    cursor.execute(f"DELETE FROM components WHERE comp_id={comp_id}")
    db.commit()
    st.success("Component deleted successfully")

st.markdown(
    """
    ## Search for a component
"""
)

comp_id = st.number_input("Component ID", key="comp_id_search")

if st.button("Search"):
    cursor.execute(f"SELECT * FROM components WHERE comp_id={comp_id}")
    component = cursor.fetchone()
    if component is None:
        st.error("Component not found")
    else:
        component_df = pd.DataFrame(
            [component],
            columns=[
                "comp_id",
                "description",
                "part_no",
                "mf_id",
                "name",
                "lifecycle",
                "category",
                "datasheet",
                "rohs",
                "mount_type",
            ],
        )
        st.dataframe(component_df)

cursor.close()
db.close()
