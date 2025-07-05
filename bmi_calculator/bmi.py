import streamlit as st
import math
import time

def bmi_c():
    st.set_page_config(page_title="Body Mass Index 𝍀 Calculator", layout="centered")
    st.title("🧮 BMI Calculator")
    st.subheader("📝 Enter Your Details")
    st.write("Calculate your Body Mass Index (BMI) and get personalized tips!")

    col1, col2 = st.columns(2)

    weight_ = col1.text_input("Enter your weight (eg. '90 kg' or '200 lbs') - ").lower().strip()
    height_ = col2.text_input("Enter your height in 'cm' or 'inches' - ").lower().strip()

    st.markdown("---")
    st.markdown("### ✅ Once you’ve entered everything, click below:")
    calculate = st.button("📩 Submit & Calculate", type="primary", use_container_width=True)
    st.markdown("---")

    if calculate:
        with st.spinner("⏳ Calculating your Body Fat %..."):
                try:
                    time.sleep(1.5)
                    if 'kg' in weight_:
                        weight = float(weight_.replace('kg','').strip())
                    elif 'lbs' in weight_ or 'lb' in weight_:
                        weight = float(weight_.replace('lbs','').replace('lb','').strip()) / 2.2
                    else:
                        weight = float(weight_)

                    if 'cm' in height_:
                        height = float(height_.replace('cm','').strip())/100
                    elif 'in' in height_ or 'inch' in height_ or 'inches' in height_:
                        height = float(height_.replace('inches', '').replace('inch', '').replace('in', '').strip()) * 2.54/100
                    else:
                        height = float(height_)/100
                    
                    if weight<=0 or height<=0:
                        st.error("❌ Please enter number greater than zero")
                        st.write("\n🔄 Let's try again...\n")
                        return
                    else:
                        bmi = weight / (height**2)
                        st.success(f"📏 Your BMI is: {bmi:.2f}")

                    st.markdown("---")

                    if bmi < 18.5:
                        st.info("\n📊 Category: Underweight")

                        st.warning("""
        ✅ Tip: You're in the 'Underweight' category.

        • Focus on high-calorie, nutritious food (nuts, dairy, lean meat).  
        • Start light strength training to build lean muscle.  
        • Sleep 7–8 hours daily for recovery.
        """)
                    elif 18.5 <= bmi < 25:
                        st.info("\n📊 Category: Normal")
                        st.warning("""
        ✅ Tip: You're in the 'Normal' category.
                                
        • Maintain balance of cardio and strength training.
        • Track calories weekly to avoid slow weight creep.
        • Consistency > perfection.\n
        """)
                    elif 25 <= bmi < 30:
                        st.info("\n📊 Category: Overweight")
                        st.warning("""
        ✅ Tip: You're in the 'Overweight' category.

        • Target 6,000–7,000 steps/day, then increase slowly.  
        • Avoid sugary drinks and processed snacks.  
        • Calorie deficit + beginner resistance training.\n
        """)
                    else:
                        st.info("📊 Category: Obese")
                        st.warning("""
        ✅ Tip: You're in the 'Obese' category.  

        • Walk daily — even 10 mins after each meal helps.  
        • Avoid crash diets — sustainable deficit is key.  
        • Focus on health markers, not just scale.
        """)

                    st.markdown("---")
                
                    with st.expander("\nℹ️ What is BMI?"):
                        st.write("""
        Body Mass Index (BMI) is a simple screening tool to estimate body fat.
        It uses your weight and height to categorize you into different health ranges.\n
                                """)
                        st.markdown("---")
                        st.write("""
        • BMI doesn't consider muscle mass, bone density, or fat distribution.
        • It's a quick estimate — not a complete diagnosis.
        • Use it with other tools like BMR, TDEE, and body measurements.\n                  
                                """)
                        with st.expander("📚Want to learn more?"):
                            st.write("""
        • BMR tells you how many calories your body burns at rest.
        • TDEE helps you set calorie goals based on your activity.
        • Muscle weighs more than fat — that's why BMI isn't perfect.
                                """)
                            
                except Exception as e:
                    st.error(f"❌ Error: {e}")
                    st.write("\n🔄 Let's try again...\n")

bmi_c()

