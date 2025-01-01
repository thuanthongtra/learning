# Databricks notebook source
# MAGIC %md
# MAGIC # Fundamentals of Data Visualization

# COMMAND ----------

# MAGIC %md
# MAGIC ## Introduction
# MAGIC **Visualization systems:** provide **_visual representations_** of datasets that helps people carry out tasks more effectively
# MAGIC
# MAGIC **A Visualization should:** provide **_insights_**, not pictures
# MAGIC 1. Save time
# MAGIC 2. Have a **_clear purpose_**
# MAGIC 3. Include only the **_relevant content_**
# MAGIC 4. Encode data/information appropriately

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Visualization Trends
# MAGIC
# MAGIC 5 Trends in Data Visualization:
# MAGIC 1. **_Communicating_** with data is a social problem, not technology problem
# MAGIC 2. **_Storytelling_** to make data more accessible
# MAGIC 3. **_Dynamic interactions_** to make data relevant
# MAGIC 4. Turning data to **_action_**
# MAGIC 5. **_Data apps_** to solve targeted solutions

# COMMAND ----------

# MAGIC %md
# MAGIC ## Good Data Visualization
# MAGIC
# MAGIC **Good visualizations:** allow users to **_see what we want them to see_** before they know that they have seen it
# MAGIC - Be strategic
# MAGIC - Shift user's attention to what you want them to see
# MAGIC
# MAGIC **Example 1:**
# MAGIC
# MAGIC ![](./images/5/Good_Data_Visualization_Example_1.png)
# MAGIC
# MAGIC **Example 2:**
# MAGIC
# MAGIC ![](./images/5/Good_Data_Visualization_Example_2.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Why Visualize?
# MAGIC - **Accurate:** Prioritize data **_accuracy_**, **_clarity_** and **_integrity_**, presenting information in a way that **_doesn't distort it_**.
# MAGIC - **Helpfull:** Help users navigate data with context and affordances that emphasize **_exploration_** and **_comparision_**
# MAGIC - **Scalable:** Adapt visualizations for different device **_sizes_**
# MAGIC
# MAGIC **Example 1:**
# MAGIC
# MAGIC ![](./images/5/Why_Visualize_Example_1.png)
# MAGIC
# MAGIC **Example 2:** 15 years of US Birth Data
# MAGIC
# MAGIC ![](./images/5/Why_Visualize_Example_2.png)
# MAGIC
# MAGIC **Example 3:** 4 years of India Birth Data
# MAGIC
# MAGIC ![](./images/5/Why_Visualize_Example_3.png)

# COMMAND ----------

# MAGIC %md
# MAGIC # Dashboard - Insights - Storytelling

# COMMAND ----------

# MAGIC %md
# MAGIC # 1. Dashboard
# MAGIC **Process:**
# MAGIC
# MAGIC ![](./images/5/Process_Dashboard.png)
# MAGIC
# MAGIC **Notes:**
# MAGIC - The results of DAR (Dashboards, Analysis, Reporting) are used for **_communicating_** and **_displaying_** to users

# COMMAND ----------

# MAGIC %md
# MAGIC **A dashboard's purpose:** should be reflected in its **_layout_**, **_style_**, and **_interaction patterns_**. 
# MAGIC - Its design should suit **_how it will be used_**, whether it’s a tool for making a presentation or deeply exploring data.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1/ Strategic
# MAGIC - Target users: **Decision makers & Senior Mgmt**
# MAGIC - Analysis type:
# MAGIC   - **High level** measure of performance
# MAGIC   - Snapshots of daily, weekly & monthly data
# MAGIC - **Tip:** get requriements from managers
# MAGIC
# MAGIC ![](./images/5/Strategic_Dashboard_Example.png)
# MAGIC
# MAGIC **Notes:**
# MAGIC - (1) Facts + Informative **_summary_**
# MAGIC - (2) **_Less filters_** + **_less details_**
# MAGIC - (3) Although metrics is about the whole company but they have **_relationships_** within the dashboard

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2/ Analytical
# MAGIC - Target users: **Mid-mgmt & Planning team**
# MAGIC - Analysis type:
# MAGIC   - **Complex data** with **rich comparison**
# MAGIC   - Interactive display and **historical** data
# MAGIC
# MAGIC ![](./images/5/Analytical_Dashboard_Example.png)
# MAGIC
# MAGIC **Notes:**
# MAGIC - (1) More **_comparisons_**
# MAGIC - (2) **_More filters_** to slice and dice

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3/ Operational
# MAGIC - Target users: **Operational workers**
# MAGIC - Analysis type:
# MAGIC   - Monitoring **activities** that are constantly changing
# MAGIC   - **Real-time** or **near real-time** data
# MAGIC
# MAGIC ![](./images/5/Operational_Dashboard_Example.png)
# MAGIC
# MAGIC **Notes:**
# MAGIC - (1) More details
# MAGIC - (2) Less filters

# COMMAND ----------

# MAGIC %md
# MAGIC ## Tips Working with User to Build Dashboard
# MAGIC **Tip 1: List metrics**
# MAGIC - Have list of metrics for each department to analyze
# MAGIC   - Ensure data team & business users to have **1 agreement** on what to show on report
# MAGIC   - Understand limitations:
# MAGIC     - **missing data** of current system, e.g. some data cannot be acquired due to systems limiations
# MAGIC     - **missing aspects** that the company does not currently applying
# MAGIC
# MAGIC ![](./images/5/List_Metrics.png)
# MAGIC
# MAGIC **Tip 2: Understand business domain**
# MAGIC - Learn from business users who have **strong domain knowledge**
# MAGIC   - Understand: process, steps, what to focus
# MAGIC
# MAGIC ![](./images/5/Understand_Business_Domain.png)
# MAGIC
# MAGIC **Tip 3: Interview User & Mockup**
# MAGIC - In order to determine this dashboard is Strategic/Analytical/Operational, we need to understand
# MAGIC   - **Objectives:** what information the dashboard will show
# MAGIC   - **Audiences:** who will use the dashboard
# MAGIC - Finalize requirement & design
# MAGIC   - To get 1st build (could cover 80-90%), then there will be adjustments
# MAGIC
# MAGIC ![](./images/5/Interview_Mockup.png)

# COMMAND ----------

# MAGIC %md
# MAGIC **Operational + Strategic:** 
# MAGIC - Very clear set of **_requirements_** or a very vague set of requirements
# MAGIC - Mockups to plan metrics
# MAGIC
# MAGIC **Analytical:** 
# MAGIC - EDA --> highlight insights
# MAGIC - Combine charts from EDA
# MAGIC
# MAGIC **Example of clear requirement:**
# MAGIC
# MAGIC ![](./images/5/Clear_Requirement_Example.png)
# MAGIC
# MAGIC **Example of mockups:**
# MAGIC
# MAGIC ![](./images/5/Mockup_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Layout
# MAGIC Try to fit it in **_16:9 ratio_**

# COMMAND ----------

# MAGIC %md
# MAGIC ### Z Scan
# MAGIC
# MAGIC ![](./images/5/Z_Scan_Example.png)
# MAGIC
# MAGIC - (1) Top Nav
# MAGIC - (2) Right Conten
# MAGIC - (3) Left Control

# COMMAND ----------

# MAGIC %md
# MAGIC ### F Scan
# MAGIC
# MAGIC ![](./images/5/F_Scan_Example.png)
# MAGIC
# MAGIC - (1) Overview
# MAGIC - (2) PKIs
# MAGIC - (3) Map
# MAGIC - (4) Slicers

# COMMAND ----------

# MAGIC %md
# MAGIC ### Others: for slicers
# MAGIC - (a) Left vertical
# MAGIC
# MAGIC ![](./images/5/Others_A.png)
# MAGIC
# MAGIC - (b) Top horizontal
# MAGIC
# MAGIC ![](./images/5/Others_B.png)
# MAGIC
# MAGIC - (c) Right vertical
# MAGIC
# MAGIC ![](./images/5/Others_C.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Designing Dashboard

# COMMAND ----------

# MAGIC %md
# MAGIC ### DAR Methodology
# MAGIC
# MAGIC 1. **Dashboard (D):** = Overview
# MAGIC     - Gives just the **_most important information_**
# MAGIC     - Has the **_least amount of Interactivity_**
# MAGIC       - Users having less time to review the status of their business
# MAGIC     - **Noted:** the wording "Dashboard" here is different of "Dashboard" in previous part (more about broader context of Strategic/Analytical/Operational)
# MAGIC
# MAGIC 2. **Analysis (A):** = Slice & Dice
# MAGIC     - Analysis pages are **_more interactive_**
# MAGIC     - Analysis pages are used to **_spend more time_** for deeper understanding
# MAGIC
# MAGIC 3. **Reporting (R):** = Most Detailed Tables
# MAGIC     - Reporting pages give the **_most granular information_** with lots of **_tabular data_**
# MAGIC     - It's where a user can spend **_a lot of time sorting and filtering_** through the details

# COMMAND ----------

# MAGIC %md
# MAGIC ### Best Practices
# MAGIC 1. **Dashboard:**
# MAGIC     - Keep the information **_general and high level_**
# MAGIC         - Just a **_few KPIs (not 20)_**
# MAGIC         - Give a **_few basic filtering_** options but not many
# MAGIC         - If possible have the page sit entirely "above the fold" of the lowest-common denominator size resolution of their organization (but this isn't critical)
# MAGIC         - Have a **_hierarchy_** to your information to make **_scanning easy_**.
# MAGIC     - The **_most important information should be larger_** than your least important information
# MAGIC
# MAGIC     ![](./images/5/BP_DAR_Dashboard_Example.png)
# MAGIC
# MAGIC 2. **Analysis:**
# MAGIC     - Introduce **_additional filters/list boxes_**
# MAGIC         - Silo information so an **_entire page_** is about a **_particular topic/theme_**
# MAGIC         - Pages can **_scroll vertically_**
# MAGIC         - Introduce **_more charts and tables_**
# MAGIC
# MAGIC     ![](./images/5/BP_DAR_Analysis_Example.png)
# MAGIC
# MAGIC 3. **Reporting:**
# MAGIC     - Give the **_most granular information_** possible
# MAGIC         - Give users the ability to view absolutely **_every detail_** they need to take action
# MAGIC
# MAGIC     ![](./images/5/BP_DAR_Reporting_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 14 Rules
# MAGIC
# MAGIC ![](./images/5/14_Rules.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 1. Consider End Goal (Type of Dashboard)
# MAGIC
# MAGIC ![](./images/5/Rule_1.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 2. Choose the Right KPI
# MAGIC **Value added by KPIs:**
# MAGIC - **Clarity:** Paint a clear picture of strategy
# MAGIC - **Focus:** Focus on what matters / requires attentions
# MAGIC - **Improvement:** Monitor process toward the desired state
# MAGIC
# MAGIC ![](./images/5/Performance.png)
# MAGIC
# MAGIC **3 Components of a KPI:**
# MAGIC - It must be **_crucial_** or key
# MAGIC - It must be **_measurable_**
# MAGIC - It must have **_some calculations_**

# COMMAND ----------

# MAGIC %md
# MAGIC **Considerations:**
# MAGIC - **Qualitative vs. quantitative metrics**
# MAGIC   - Qualitative metrics are unstructured, anecdotal (VN giai thoai), revealing, and **_hard to aggregate_**
# MAGIC   - Quantitative metrics involve **_numbers_** and **_statistics_** and provide hard numbers but **_less insight_**
# MAGIC - **Vanity vs. actionable metrics**
# MAGIC   - Vanity (VN phu phiem) metrics might make you feel good, but they **_don't change how you act_**
# MAGIC     - e.g. **_total_** signups, **_number_** of active users --> just for "FYI"
# MAGIC   - Actionable metrics change your behavior by helping you pick a **_course of action_**
# MAGIC     - e.g. **_percent_** of users who are active --> next action: investigate whether number of active users increases/decreases or total users increases/decreases
# MAGIC - **Exploratory vs. reporting metrics**
# MAGIC   - Exploratory metrics are speculative (VN suy doan) and try to **_find unknown insights_**
# MAGIC   - Reporting metrics keep you abreast (VN chung chung) of normal, managerial, day-to-day operations
# MAGIC - **Lagging vs. leading metrics**
# MAGIC   - Lagging metrics explain the **_past_**
# MAGIC   - Leading metrics give you a **_predictive understanding_** of the future (can be **_target_**)
# MAGIC     - Leading metrics are better because you still have time to act on them-the horse hasn't left the barn yet
# MAGIC - **Correlated vs. causal metrics**
# MAGIC   - If
# MAGIC     - Two metrics **_change together_** --> they're **_correlated_**
# MAGIC     - One metric **_causes_** another metric to **_change_** --> they're **_causal_**
# MAGIC   - If you find a causal relationship between **_something you want_** (like revenue) and **_something you can control_** (like which ad you show) --> you can **_change the future_**

# COMMAND ----------

# MAGIC %md
# MAGIC #### 3. Don't Try to Place All The Information on The Same Page
# MAGIC
# MAGIC ![](./images/5/Rule_3.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 4. Provide Context
# MAGIC **Text is your friend**
# MAGIC
# MAGIC ![](./images/5/Rule_4.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 5. Make It As Easy As Possible
# MAGIC
# MAGIC Always try to put yourself in the user's position
# MAGIC
# MAGIC ![](./images/5/Rule_5.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 6. Choose Your Layout Carefully
# MAGIC
# MAGIC **Pay attention to attention:** positioning the most important information where people look first
# MAGIC - User **_looks first_** for information on the **_top and left side_**
# MAGIC - User also focus their attention **_down the left_**
# MAGIC - The **_center_** gets fair bit of attention as well
# MAGIC - **_Bottom and right_** may **_not be noticed_** by user
# MAGIC
# MAGIC ![](./images/5/Rule_6_Attention_Example.png)
# MAGIC
# MAGIC **Grids:** a series of columns and "gutters" of certain widths
# MAGIC - To ensure that key lines in their design align
# MAGIC - To bring a coherence and order to the page that puts users at ease
# MAGIC
# MAGIC ![](./images/5/Rule_6_Grid_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 7. Prioritize Simplicity
# MAGIC **Remove to Improve**
# MAGIC - Remove background
# MAGIC - Remove redundant lables
# MAGIC - Remove borders
# MAGIC - Remove colours
# MAGIC - Remove special effects
# MAGIC - Remove bold
# MAGIC - Lighten lables
# MAGIC - Lighten / remove lines
# MAGIC - Direct label
# MAGIC
# MAGIC ![](./images/5/Rule_7_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 8. Be Careful With Colours
# MAGIC **Choose a few and stick with them**
# MAGIC
# MAGIC ![](./images/5/Rule_8_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 9. Don't Overuse Real-time Data
# MAGIC
# MAGIC Unless you're tracking some live results, most dashboards don't need to be updated continually
# MAGIC
# MAGIC ![](./images/5/Rule_9_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 10. Use The Right Type of Chart
# MAGIC
# MAGIC ![](./images/5/Rule_10.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 11. Be Consisten With Labeling and Data Formatting
# MAGIC
# MAGIC ![](./images/5/Rule_11_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 12. Use Interface Elements
# MAGIC Consider to allow users to access Power BI in multiple devices
# MAGIC
# MAGIC ![](./images/5/Rule_12.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 13. Double Up Your Margins
# MAGIC
# MAGIC **White space:** can be used to delineate sections or help users see grouping of content in a dashboard
# MAGIC - Using white space = creating places for the **_eye to "rest"_** so that non-white space have **_more impact_**
# MAGIC - Using white space = **_sacrificing_** extra **_chart or metric_**, but it can make huge difference in user comprehension
# MAGIC
# MAGIC ![](./images/5/Rule_13.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 14. Never Stop Evolving
# MAGIC The digital world is ever-evolving. 
# MAGIC - Change is constant, and the principles of effective dashboards are dictated by a willingness to improve and enhance your design efforts continuously.

# COMMAND ----------

# MAGIC %md
# MAGIC # 2. Insights (BUS)
# MAGIC **Process:**
# MAGIC
# MAGIC ![](./images/5/Process_Insights.png)
# MAGIC
# MAGIC **Notes:**
# MAGIC - We look back at the **_Bookmarks_** that we made in **_EDA (Data Analytics Taxonomy)_** step to **_re-observe_** whether there are **_insights_**?

# COMMAND ----------

# MAGIC %md
# MAGIC **Insights must be:**
# MAGIC 1. **BIG:**
# MAGIC     - The analysis must be **_statisticall significant_** and **_numerically significant_**
# MAGIC     - We want a result that **_subtantially change the outcome_**
# MAGIC 2. **USEFUL:** **_Actionable?_**
# MAGIC     - What should the audience do **_after hearing the insight_**?
# MAGIC     - Can they take an action that improves their objective?
# MAGIC     - Even if it's informational, what should they do next?
# MAGIC 3. **SURPRISING:**
# MAGIC     - Is this something they **_didn't know_**? Is it **_non-obvious_**?
# MAGIC     - Does it overturn a **_domain-driven belief_** or a gut feel?
# MAGIC     - Or does it bring consensus to a group with divided opinion?
# MAGIC
# MAGIC **Example:** Only those that are **_HIGH_** or **_MEDIUM_** on **_ALL ASPECTS_** are Insights
# MAGIC
# MAGIC ![](./images/5/Insight_Example_1.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Case Study 1
# MAGIC
# MAGIC ![](./images/5/Insights_Case_Study_1.png)
# MAGIC
# MAGIC **Notes:**
# MAGIC - **Data Exploration:** there was **_abnormal trend_** of data in later period in **_Actual_**
# MAGIC - **Insight or Not:**
# MAGIC   - International reseller with **_40%_** contribution --> Big = high
# MAGIC   - We can upsale this group --> Useful = high
# MAGIC   - New trend --> Surprising = high

# COMMAND ----------

# MAGIC %md
# MAGIC ## Case Study 2
# MAGIC
# MAGIC ![](./images/5/Insights_Case_Study_2.png)
# MAGIC
# MAGIC **Notes:**
# MAGIC - **Data Exploration:** can be **_Bias_** because not sure Clinic#1 (which have doctor) has more mortality
# MAGIC - **Next Step:** 
# MAGIC   - Check raw data to ensure data is correct
# MAGIC   - Look as different aspects in case Clinic#1 has **_more difficult_** cases

# COMMAND ----------

# MAGIC %md
# MAGIC ## How to Find Insights?

# COMMAND ----------

# MAGIC %md
# MAGIC ### BI Taxonomy
# MAGIC
# MAGIC ![](./images/5/Process_BI_Taxonomy.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 1. MECE + Right Chart, Right Information

# COMMAND ----------

# MAGIC %md
# MAGIC ##### 1. Change dimension
# MAGIC To have other perspectives. For example
# MAGIC   - Change chart orientation: Year/Product -> Product/Year
# MAGIC     
# MAGIC     ![](./images/5/Change_Dimension_Example_1.png)
# MAGIC
# MAGIC   - Change categories: customer -> product
# MAGIC
# MAGIC     ![](./images/5/Change_Dimension_Example_2.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### 2. Change level detail of data 
# MAGIC
# MAGIC For example:
# MAGIC - **Before:** view by **_Year_** --> not the same base to compare, e.g. **_Lincoin Memorial_** opened in **_1960_** while **_Jefferson_** opened in **_2000_** --> not fair comparison
# MAGIC
# MAGIC ![](./images/5/Change_Level_Detail_Example_1.png)
# MAGIC
# MAGIC - **After:** view by **_number of Years has been opened_** --> same base --> fair
# MAGIC
# MAGIC ![](./images/5/Change_Level_Detail_Example_2.png)
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##### 3. Choose the Right Chart
# MAGIC For example, showing Sales for each Category
# MAGIC
# MAGIC ![](./images/5/Choose_The_Right_Chart_Example.png)
# MAGIC
# MAGIC **Notes:**
# MAGIC - Left chart: only shows **_total sales_**
# MAGIC - Right chart: can see the **_growth of sales_**

# COMMAND ----------

# MAGIC %md
# MAGIC ##### 4. Break Data by Multiples
# MAGIC
# MAGIC ![](./images/5/Break_Data_By_Multiples_Example.png)
# MAGIC
# MAGIC **Notes:**
# MAGIC - Left chart: **_hard to see_** the trend, distribution of data
# MAGIC - Middle chart: break into **_Income Group_**
# MAGIC - Right chart: break into **_Region_**

# COMMAND ----------

# MAGIC %md
# MAGIC #### 2. Type of Insights Supported by Power BI

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Get Quick Insight
# MAGIC In PBI Service, we can get quick insights as:
# MAGIC
# MAGIC ![](./images/5/Get_Quick_Insight.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Category Outliers (Top/Bottom)
# MAGIC Highlight cases where 1 or 2 categories have **_much larger or lower_** than others
# MAGIC
# MAGIC ![](./images/5/Category_Outlier_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Change Points in a Time series
# MAGIC Highlights when there are significant **_changes in trends_** in a time series data
# MAGIC
# MAGIC ![](./images/5/Change_Point_In_Time_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Seasonality in Time Series
# MAGIC Finds **_periodic patterns_** in time series data, such as weekly, monthly, or yearly seasonality.
# MAGIC
# MAGIC ![](./images/5/Seasonality_in_Time_Searis_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Time Series Outliers
# MAGIC For data across a time series, detects when there are **_specific dates or times_** with values **_significantly different_** than the other date/time values.
# MAGIC
# MAGIC ![](./images/5/Time_Series_Outlier_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Correlation
# MAGIC
# MAGIC Detects cases where **_multiple measures_** show a **_similar pattern_** or **_trend_** when plotted **_against a category_** or value in the dataset.
# MAGIC
# MAGIC ![](./images/5/Correlation_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Low Variance
# MAGIC Detects cases where data points for a dimension **_aren't far_** from the **mean**, so the **_"variance" is low_**.
# MAGIC
# MAGIC - **Example:** Let's say you have the measure "sales" and a dimension "region". 
# MAGIC   - And looking across region you see that there is very little difference between the data points and the mean (of the data points). 
# MAGIC   - The insight triggers when the variance of sales across all regions is below a threshold. In other words, when sales are pretty similar across all regions.
# MAGIC
# MAGIC ![](./images/5/Love_Variance_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Analyze Function
# MAGIC
# MAGIC ![](./images/5/Analyze_Function_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Smart Narrative Function
# MAGIC
# MAGIC ![](./images/5/Smart_Narrartive_Function_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adjust the Underlying Data
# MAGIC 5 Data Variations to Consider:
# MAGIC - Totals
# MAGIC - % Change
# MAGIC - Calculated Metric (Ratio)
# MAGIC - Added Context
# MAGIC - Variance
# MAGIC
# MAGIC ![](./images/5/Data_Variation_To_Consider.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 1. Totals
# MAGIC Get **_aggretations_** of measures
# MAGIC
# MAGIC **Example 1:**
# MAGIC
# MAGIC ![](./images/5/Total_Example_1.png)
# MAGIC
# MAGIC **Notes:**
# MAGIC - In this dual y-axis chart, both revenue and number of customer have grown throughout the year. However, **_revenue isn't growing_** as fast the the **_customer base is expanding_**
# MAGIC - It's **_difficult to see_** that the monthly revenue isn't expanding as rapidly as the customer base because each metric has a **_different scale_**
# MAGIC
# MAGIC **Example 2:** similar issue, hard to see
# MAGIC
# MAGIC ![](./images/5/Total_Example_2.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 2. % Change
# MAGIC
# MAGIC To show the differences between the growth rates of each metric, you could change the data to **_percent change_** rather than using **_total amounts_**. 
# MAGIC - With percent change, you can have metrics with different base units share a **_common axis_**, making it **_easier to compare changes_** between the metrics.
# MAGIC - However, in this case, using percent change also **_somewhat hides the impact_** to the business.
# MAGIC
# MAGIC ![](./images/5/Percent_Change_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 3. Calculated Metric (Ratio)
# MAGIC
# MAGIC An alternative approach is to create a **_calculated metric or ratio_**, such as revenue per customer, to tell the story **_more dramatically_**. 
# MAGIC
# MAGIC - Instead of relying on just totals, showing the percent change or creating a calculated metric may be a better option for communicating your keypoints.
# MAGIC
# MAGIC ![](./images/5/Calculated_Metric_Example.png)
# MAGIC
# MAGIC **Notes:**
# MAGIC - You can see revenue per customer has decreased significantly during the year, even though the monthly revenue has risen steadily.
# MAGIC - In other words, by trending the revenue per customer on the 2nd axis, it's easier to see the company is acquiring more customers that spend less

# COMMAND ----------

# MAGIC %md
# MAGIC #### 4. Added Context
# MAGIC Add context can **_change the message_**
# MAGIC
# MAGIC ![](./images/5/Added_Context_Example.png)
# MAGIC
# MAGIC **Notes:**
# MAGIC - The 2 charts shows 
# MAGIC   - **_column chart of Revenue (2018)_** 
# MAGIC   - added context **_2 lines of Revenue per Customer (2017 and 2018)_**
# MAGIC - It shows the presence of contextual data impacts what is communicates

# COMMAND ----------

# MAGIC %md
# MAGIC #### 5. Variance
# MAGIC
# MAGIC Do the **_math for your audience_**
# MAGIC
# MAGIC **Example 1:** Left chart shows **_pure sum of 2 years_**, right charts shows **_difference sum of 2 years_**
# MAGIC
# MAGIC ![](./images/5/Varience_Example_1.png)
# MAGIC
# MAGIC
# MAGIC **Example 2:** Left chart shows **_Revenue_**, right charts shows **_Profit_**
# MAGIC
# MAGIC ![](./images/5/Varience_Example_2.png)
# MAGIC
# MAGIC **Example 3:** 
# MAGIC
# MAGIC ![](./images/5/Varience_Example_3.png)

# COMMAND ----------

# MAGIC %md
# MAGIC # 3. Storytelling
# MAGIC ![](./images/5/Process_Storytelling.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Dashboards Are Not Data Stories
# MAGIC Do not expect a dashboard by itself to create action to be taken
# MAGIC   - PBI Dashboard can be the **_foundation_** of your **_Data Stories_**
# MAGIC
# MAGIC ![](./images/5/Dashboards_Not_Stories.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Design a Data Story
# MAGIC
# MAGIC ![](./images/5/StoryFraming_StoryTelling.png)
# MAGIC
# MAGIC **Data Story Architect:** goal = **_Reduce time_** to get to Data Story
# MAGIC
# MAGIC ![](./images/5/Goal_Data_Story_Architect.png)

# COMMAND ----------

# MAGIC %md
# MAGIC **Freytag's Pyramid:**
# MAGIC
# MAGIC ![](./images/5/Turn_Findings_To_Data_Story.png)

# COMMAND ----------

# MAGIC %md
# MAGIC **Example 1:**
# MAGIC
# MAGIC ![](./images/5/Turn_Findings_To_Data_Story_Example_1.png)

# COMMAND ----------

# MAGIC %md
# MAGIC **Example 2:**
# MAGIC
# MAGIC ![](./images/5/Turn_Findings_To_Data_Story_Example_2.png)

# COMMAND ----------

# MAGIC %md
# MAGIC **Data Storytelling Framework**
# MAGIC
# MAGIC ![](./images/5/Data_Storytelling_Framework.png)
# MAGIC
# MAGIC **Notes:**
# MAGIC - In the process of Build a Data Story, we move Aha Moment at 1st to get a focus what to present, then we add more points to prove it
# MAGIC - In the framework, we need to pick within our findings what to be the BUS (Big, Useful, Surprising)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 1: Identify Aha Moment

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 2: Find Your Beginning and Setting

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Select Your Rising Insights

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 4: Empower Your Audience to Act

# COMMAND ----------

# MAGIC %md
# MAGIC ### Example
# MAGIC **E-commerce**

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exploratory vs. Explanatory Analysis

# COMMAND ----------

# MAGIC %md
# MAGIC # Visualization Principles

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Gestalt Laws
# MAGIC
# MAGIC **Preattentive attributes:** help people **_discern similarities and difference_** in data visualization
# MAGIC
# MAGIC ![](./images/5/Common_Preattentive_Attributes.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Visual Cues
# MAGIC
# MAGIC **Graphical Methods Vary In Effectiveness:**
# MAGIC
# MAGIC ![](./images/5/Graphical_Methods_Vary_In_Effectiveness.png)

# COMMAND ----------

# MAGIC %md
# MAGIC **Visual Cues Ranked:**
# MAGIC
# MAGIC ![](./images/5/Visual_Cues_Ranked.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. How Chart Lies

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Line Chart
# MAGIC
# MAGIC **Example 1:** **_separate_** into 2 charts
# MAGIC
# MAGIC ![](./images/5/Line_Chart_Example_1.png)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Example 2:** combine into **_1 axis_**
# MAGIC
# MAGIC ![](./images/5/Line_Chart_Example_2.png)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Example 3:** change charts
# MAGIC
# MAGIC ![](./images/5/Line_Chart_Example_3.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Scatter Chart
# MAGIC **Example 1:** 
# MAGIC - Left chart = all countries without color density
# MAGIC - Right chart = add color intensity --> but not so clear
# MAGIC
# MAGIC ![](./images/5/Scatter_Chart_Example_1.png)

# COMMAND ----------

# MAGIC %md
# MAGIC **Example 2:** Separate 3 types of income countries
# MAGIC
# MAGIC ![](./images/5/Scatter_Chart_Example_2.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Spatial Chart
# MAGIC **Example:**
# MAGIC - Left chart = hard to see votes of the 2
# MAGIC - Middle + right chart = separate, clearer
# MAGIC
# MAGIC ![](./images/5/Spatial Chart_Example_1.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Axis, Data Cuts
# MAGIC
# MAGIC **Example 1:** Choose the right range of axises
# MAGIC
# MAGIC ![](./images/5/Axis_Data_Cuts_Example_1.png)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Example 2:** Choose the right range of axises
# MAGIC
# MAGIC ![](./images/5/Axis_Data_Cuts_Example_2.png)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Example 3:** Choose the right data cut
# MAGIC
# MAGIC ![](./images/5/Axis_Data_Cuts_Example_3.png)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Example 4:** Choose the right data cut
# MAGIC - The inauguration had been increased before Trump was president, not because of him, it increases
# MAGIC
# MAGIC ![](./images/5/Axis_Data_Cuts_Example_4.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. Color/Labels
# MAGIC
# MAGIC **Example:** choose the right color density
# MAGIC
# MAGIC ![](./images/5/Color_Label.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 6. Selected Numbers
# MAGIC
# MAGIC **Example:** should illustrate the **_"full picture"_**
# MAGIC
# MAGIC ![](./images/5/Selected_Number_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Color

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Color Introduction
