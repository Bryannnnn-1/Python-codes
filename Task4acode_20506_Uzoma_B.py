#Import the necessary python libraries
#import pandas as pd
import csv
import matplotlib.pyplot as plt


#Validate if the file is in the correct path
try:
    df = pd.read_csv('Task4a_data.csv')
except FileNotFoundError:
    print("CSV file not found. Please ensure 'Task4a_data.csv' is in the correct path")
    print("Save it in same folder as your python script or provide the correct path")
    exit()#End the code if FileNotFoundError is triggered


# Outputs the initial menu and validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("################## Botes Parcels CRM System ####################")
        print("####################################################")
        print()
        print("########### Please select an option ################")
        print("### [1].  Total issues by type")
        print("### [2].  Display all stats in text form")
        print("### [3].  Visualise issues and solution based on region ")
        print("### [4].  Visualise the average time taken to resolve different types of issue")
        print("### [5].  Visualise Issue Type and its frequency ")
        print("### [6].  Visualise Resolution Type and its frequency")
        print("### [7].  Exit")
        print()
        print("Choose from 1 - 7")

        choice = input('Enter your number selection here: ')

        try:#validate the user input to allow only integers
            choice = int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            print()
            flag = True
        else:
            if choice not in [1, 2, 3, 4, 5, 6, 7]:
                print("Invalid Choice!")
                print()
                flag = True
            else:
                print('Choice accepted!')
                print()
                flag = False
    return choice#return value to be used in another function of the prgram

# Submenu for totals, provides type check validation for the input and returns issue type as a string
def total_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total issues by type ################")
        print("####################################################")
        print()
        print("########## Please select an issue type ##########")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

        choice = input('Enter your number selection here: ')

        try:#validating the iser input
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            print()
            flag = True
        else:    
            print('Choice accepted!')
            print()
            choice = int(choice)
            flag = False
    #create a  list to store the issue types
    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    issueType = issueTypeList[choice-1]#subtract 1 from the user input and index it to the list. python list is indexed 0
    return issueType#return value to be used in another function of the prgram     


def graph():
    flag = True

    while flag:
        print("~~~~~~~~~~~~~~Which type of graph would you like to visualise the data~~~~~~~~~~~~~~")
        print()
        print("[1].  Bar chart")
        print("[2].  Pie Chart")
        print("[3].  line Graph")        
        print("[4].  Go back to Main menu")
        print()
        print("Choose from 1 - 4")

        try:#validate user input
            graph_choice = int(input(">>>>> "))
        except ValueError:
            print("Invalid Input!\nTry again!")
        else:
            if  graph_choice not in [1, 2, 3, 4]:
                print("Choose within the range (1 - 4)!\nTry again")
                print()
                flag = True
            else:
                flag = False#start the loop again
                
                return graph_choice#return value to be used in another function of the prgram


def region():

    #list of regions
    regions = [
        "South West",
        "West Midland",
        "London",
        "North Wales",
        "South West",
        "East of England",
        "North East",
        "East Midlands",
        "Yorkshire and the Humber",
        "South Wales",
        "Northern Ireland",
        "Scotland",
        "North West"
    ]

    flag = True

    while flag:
        print("~~~~~~~~~~~~~~Which region do you want to see~~~~~~~~~~~~~~")
        print()
        print("[1].  South West")
        print("[2].  West Midland")
        print("[3].  London")
        print("[4].  North Wales")
        print("[5].  South West")
        print("[6].  East of England")
        print("[7].  North East")
        print("[8].  East Midlands")
        print("[9].  Yorkshire and the Humber")
        print("[10].  South Wales")
        print("[11].  Northern Ireland")
        print("[12].  Scotland")
        print("[13].  North West")
        print()
        print("Choose from 1 - 13")

        try:#validating the user input
            region_choice = int(input(">>>>> "))
        except ValueError:
            print("Invalid Input!\nTry again!")
        else:
            if  region_choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:#if the input number not in the list
                print("Choose within the range (1 - 13)!\nTry again")#error messgae
                print()
                flag = True
            else:
                
                selected_region = regions[region_choice - 1]#indexing the user input properly so it will return the value from the liwst
                filtered_df = df[df['Region'] == selected_region]
                flag = False
                
                return selected_region, filtered_df#returning the value to be used in another function
            
# Creates a new dataframe then counts the number of occurences of the requested issue type

def get_total_data(total_menu_choice):
    
    issues = pd.read_csv("Task4a_data.csv")#reading the csv
    
    total = issues['Issue Type'].value_counts()[total_menu_choice]

    msg = "The total number of issues logged as a {} was: {}".format(total_menu_choice, total)
    return msg

#Function to loop through the "Issue Type"column and count the
#issue type while updating the counter
def issue_counter():
    #initialise counters
    delivery_issue = 0
    customer_account_issue = 0
    service_complaint = 0
    collection_issue = 0
    
    issue_dict = {}
    
    for issue in df["Issue Type"]:#for loop to loop through the column
        if pd.isna(issue):
            continue#to skip empty columns if any
        elif issue == "Delivery Issue":
            delivery_issue += 1#update the counter
        elif issue == "Customer Account Issue":
            customer_account_issue += 1#update the counter
        elif issue == "Service Complaint":
            service_complaint += 1#update the counter
        elif issue == "Collection Issue":
            collection_issue  += 1#update the counter

    issue_dict.update({"Delivery Issue" : delivery_issue})
    issue_dict.update({"Customer Account Issue" : customer_account_issue})
    issue_dict.update({"Service Complaint" : service_complaint})
    issue_dict.update({"Collection Issue" : collection_issue})


    #returning the dictionary to be used in another section of the code
    return issue_dict

#Function to loop through the "How Resolved"column and count the
#resolution method while updating the counter
def solution_counter():
    #initialise counters
    full_refund = 0
    account_updated = 0
    partial_refund = 0
    manual_password_username_reset = 0
    automated_password_username_reset = 0
    solution_dict = {}
    
    for solution in df["How Resolved"]:#loop through the column
        if pd.isna(solution):
            continue#to skip empty columns if any
        elif solution == "Full Refund Issued":
            full_refund += 1#update the counter
        elif solution == "Account Updated":
            account_updated+= 1#update the counter
        elif solution == "Partial Refund Issued":
            partial_refund += 1#update the counter
        elif solution == "Manual Password/Username Reset":
            manual_password_username_reset += 1#update the counter
        elif solution == "Automated Password/Username Reset":
            automated_password_username_reset += 1#update the counter

    #updating dictionary
    solution_dict.update({"Full Refund Issued" : full_refund})
    solution_dict.update({"Account Updated" : account_updated})
    solution_dict.update({"Partial Refund Issued" : partial_refund})
    solution_dict.update({"Manual Password/Username Reset" : manual_password_username_reset})
    solution_dict.update({"Automated Password/Username Reset" : automated_password_username_reset})
        
    #returning the dictionary to be used in another section of the code
    return solution_dict


def avg_day_to_resolve_by_issue_type():
    
    issue_days_dict = {}# Initialize an empty dictionary
    selected = df.groupby('Issue Type')['Days To Resolve'].mean().reset_index()# Group by Issue Type and calculate the average Days To Resolve
    for index, row in selected.iterrows():# Loop through the selected DataFrame manually
        issue_type = row['Issue Type']
        avg_days = row['Days To Resolve']
        issue_days_dict[issue_type] = avg_days

    return issue_days_dict, selected#return values needed in another section


def issue_counter_by_region():
    region_issue_dict = {}# Initialize an empty dictionary
    for region, group in df.groupby('Region'):# Group by region and count issues in each region
        issue_counts = group['Issue Type'].value_counts().to_dict()#count the columns and turn to a dictionary
        region_issue_dict[region] = issue_counts
    
    return region_issue_dict#return values needed in another section


def solution_counter_by_region():
    region_solution_dict = {}# Initialize an empty dictionary
    for region, group in df.groupby('Region'):# Group by region and count solutions in each region
        solution_counts = group['How Resolved'].value_counts().to_dict()#count the columns and turn to a dictionary
        region_solution_dict[region] = solution_counts
    
    return region_solution_dict#return values needed in another section


#ttis function will display all the outputs in text
def display_stats_in_text(solution_dict, issue_dict, issue_days_dict,
                          region_issue_dict, region_solution_dict):
    
    print("RESOLUTION METHOD FREQUENCY\n")
    for key, value in solution_dict.items():#loop and display the resolution
        print(f"~~ {key}: {value}")

    print()
    print("ISSUE TYPEE FREQUENCY\n")
    for key, value in issue_dict.items():#loop the dict and display
        print(f"~~ {key}: {value}")

    print()
    print("ISSUE TYPEE AND DAYS TAKEN TO RESOLVE\n")
    for key, value in issue_days_dict.items():#loop the dict and display
        print(f"~~ {key}: {value:.2f} days")

    print()
    max_issue_key = max(issue_dict, key=issue_dict.get)
    max_issue_value = issue_dict[max_issue_key]
    print(f"The Issue that occured the most is '{max_issue_key}' which occured '{max_issue_value}' times")#printing the max solution

    print()#printing the max solution
    max_solution_key = max(solution_dict, key=solution_dict.get)
    max_solution_value = solution_dict[max_solution_key]
    print(f"The most common way used to resolve is '{max_solution_key}' which occured '{max_solution_value}' times")

    print()

#ploting and display the pie chart
def pie_chart_for_issue_by_region(filtered_df, selected_region):
        region_issue_counts = filtered_df["Issue Type"].value_counts()
        df = pd.DataFrame(region_issue_counts).reset_index()
        df.columns = ["Issue Type", "Frequency"]
        df.set_index("Issue Type").plot.pie(
            y = "Frequency",
            autopct="%1.1f%%",
            legend=False,
            startangle=140,
            figsize=(10, 6)
        )
        plt.title(f"Issue Type Distribution for Region: {selected_region}")
        plt.show()

#ploting and display the pie chart
def pie_chart_for_solution_by_region(filtered_df, selected_region):
        region_solution_counts = filtered_df["How Resolved"].value_counts()
        df = pd.DataFrame(region_solution_counts).reset_index()
        df.columns = ["How Resolved" , "Frequency"]
        df.set_index("How Resolved").plot.pie(
            y="Frequency",
            autopct="%1.1f%%",
            legend=False,
            startangle=140,
            figsize=(10, 6)
        )
        plt.title(f"Resolution Method Distribution for Region: {selected_region}")
        plt.show()


def bar_chart_for_solution_by_region(filtered_df, selected_region):
        region_solution_counts = filtered_df["How Resolved"].value_counts()
        df = pd.DataFrame(region_solution_counts).reset_index()
        df.columns = ["How Resolved" , "Frequency"]
        plt.figure(figsize=(10, 6))
        plt.bar(df["How Resolved"], df["Frequency"], color="blue", )
        plt.title(f"Resolution Method Frequency for Region: {selected_region}")
        plt.xticks(rotation=45)
        plt.xlabel("Resolution Method")
        plt.ylabel("Frequency")
        plt.show()


def bar_chart_for_issue_by_region(filtered_df, selected_region):
        region_issue_counts = filtered_df["Issue Type"].value_counts()
        df = pd.DataFrame(region_issue_counts).reset_index()
        df.columns = ["Issue Type", "Frequency"]
        plt.figure(figsize=(10, 6))
        plt.bar(df["Issue Type"], df["Frequency"], color="blue")
        plt.title(f"Issue Type Frequency for Region: {selected_region}")
        plt.xticks(rotation=45)
        plt.xlabel("Issue Type")
        plt.ylabel("Frequency")
        plt.show()

        
def bar_chart_avg_time_by_issue_type(issue_days_dict):
    df = pd.DataFrame(list(issue_days_dict.items()), columns=["Issue Type", "Avg Time to Resolve"])
    plt.figure(figsize=(10, 6))
    plt.bar(df["Issue Type"], df["Avg Time to Resolve"], color="purple")
    plt.title("Average Time to Resolve by Issue Type")
    plt.xticks(rotation=45)
    plt.xlabel("Issue Type")
    plt.ylabel("AVERAGE TIME TO RESOLVE BY ISSUE TYPE (DAYS)")
    plt.show()

#ploting and display the pie chart
def pie_chart_avg_time_by_issue_type(issue_days_dict):
    df = pd.DataFrame(list(issue_days_dict.items()), columns=["Issue Type", "Avg Time to Resolve"])
    df.set_index("Issue Type").plot.pie(
        y="Avg Time to Resolve",
        autopct="%1.1f%%",
        legend=False,
        startangle=140,
        figsize=(10, 6)
    )
    plt.ylabel(" ")
    plt.title("AVERAGE TIME TO RESOLVE BY ISSUE TYPE (DAYS)")
    plt.show()


def line_graph_avg_time_by_issue_type(issue_days_dict):
    df = pd.DataFrame(list(issue_days_dict.items()), columns=["Issue Type", "Avg Time to Resolve"])
    plt.figure(figsize=(10, 6))
    plt.plot(df['Issue Type'], df['Avg Time to Resolve'], marker="o", color="green", linestyle="-")
    plt.title("AVERAGE TIME TO RESOLVE BY ISSUE TYPE (DAYS)")
    plt.xlabel("Issue Type")
    plt.ylabel("Average Time to Resolve (Days)")
    plt.xticks(rotation=45)
    plt.show()
    
#plot and dsplay line graph for soltuion by region
def line_graph_for_solution_by_region(filtered_df, selected_region):
    region_solution_counts = filtered_df["How Resolved"].value_counts()
    df = pd.DataFrame(region_solution_counts).reset_index()
    df.columns = ["How Resolved", "Frequency"]
    plt.figure(figsize=(10, 6))
    plt.plot(df["How Resolved"], df["Frequency"], marker= "o", color="blue", linestyle="-")
    plt.title(f"Resolution Method Frequency for Region: {selected_region}")
    plt.xlabel("Resolution Method")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.show()

#plot and dsplay line graph for issue by region
def line_graph_for_issue_by_region(filtered_df, selected_region):
    region_solution_counts = filtered_df["Issue Type"].value_counts()
    df = pd.DataFrame(region_solution_counts).reset_index()
    df.columns = ["Issue Type", "Frequency"]
    plt.figure(figsize=(10, 6))
    plt.plot(df["Issue Type"], df["Frequency"], marker="o", color="blue", linestyle="-")
    plt.title(f"Issue Type Frequency for Region: {selected_region}")
    plt.xlabel("Resolution Method")
    plt.ylabel("Frequency")
    plt.xticks(rotation=35)
    plt.show()

#plot and display bar chart for issue
def bar_chart_for_issue(issue_dict):
    df = pd.DataFrame(list(issue_dict.items()), columns=["Issue Type", "Frequency"])
    plt.figure(figsize=(10, 6))
    plt.bar( df["Issue Type"], df["Frequency"], color="blue")
    plt.title("BAR CHART SHOWING ISSUE TYPE FREQUENCY")
    plt.xticks(rotation=45)
    plt.xlabel("Issue Type")
    plt.ylabel("Frequency")
    plt.show()

#plot and display bar chart for solution
def bar_chart_for_solution(solution_dict):
    df = pd.DataFrame(list(solution_dict.items()), columns=["How Resolved", "Frequency"])
    plt.figure(figsize=(10, 6))
    plt.bar( df["How Resolved"], df["Frequency"], color="green")
    plt.title("BAR CHART SHOWING RESOLUTION METHOD FREQUENCY")
    plt.xticks(rotation=45)
    plt.xlabel("How Resolved")
    plt.ylabel("Frequency")
    plt.show()

#ploting and display the pie chart for issue
def pie_chart_for_issue(issue_dict):
    df = pd.DataFrame(list(issue_dict.items()), columns=["Issue Type", "Frequency"])
    df.set_index("Issue Type").plot.pie(
        y="Frequency",
        autopct="%1.1f%%",
        legend=False,
        startangle=140,
        figsize=(10, 6)
        )
    plt.title('PIE CHART SHOWING ISSUE TYPE DISTRIBUTION')
    plt.show()

#ploting and display the pie chart
def pie_chart_for_solution(solution_dict):
    df = pd.DataFrame(list(solution_dict.items()), columns=["How Resolved", "Frequency"])
    df.set_index("How Resolved").plot.pie(
        y="Frequency",
        autopct="%1.1f%%",
        legend=False,
        startangle=140,
        figsize=(10, 6)
        )
    plt.title("PIE CHART SHOWING RESOLUTION METHOD DISTRIBUTION")
    plt.show()

#plot and dsplay line graph
def line_graph_for_solution(solution_dict):
    df = pd.DataFrame(list(solution_dict.items()), columns=["How Resolved", "Frequency"])
    df = df.sort_values(by="Frequency", ascending=True)
    plt.figure(figsize=(10, 6))
    plt.plot(df["How Resolved"], df["Frequency"], marker='o', color='blue', linestyle='-')
    plt.title("Line Graph Showing Resolution Method Frequency")
    plt.xlabel("Resolution Method")
    plt.ylabel("Frequency")
    plt.xticks(rotation=35)
    plt.show()

#plot and dsplay line graph
def line_graph_for_issue(issue_dict):
    df = pd.DataFrame(list(issue_dict.items()), columns=["Issue Type", "Frequency"])
    df = df.sort_values(by="Frequency", ascending=True)
    plt.figure(figsize=(10, 6))
    plt.plot(df["Issue Type"], df["Frequency"], marker='o', color='blue', linestyle='-')
    plt.title("Line Graph Showing Resolution Method Frequency")
    plt.xlabel("Resolution Method")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.show()


flag = True
while flag:
    #calling the menu to start the code
    main_menu_choice = main_menu()

    #passing of argument and calling of functions
    if main_menu_choice ==  1:
        total_menu_choice = total_menu()
        print(get_total_data(total_menu_choice))

    elif main_menu_choice == 2:
        issue_dict = issue_counter()
        solution_dict = solution_counter()
        region_solution_dict = solution_counter_by_region()
        region_issue_dict = issue_counter_by_region()
        issue_days_dict, selected = avg_day_to_resolve_by_issue_type()
        display_stats_in_text(solution_dict, issue_dict, issue_days_dict, region_issue_dict, region_solution_dict)

    elif main_menu_choice == 3:
        selected_region, filtered_df = region()
        region_solution_dict = solution_counter_by_region()
        region_issue_dict = issue_counter_by_region()
        graph_choice = graph()
        if graph_choice == 1:
            print("~~~~~~~~~~~~2 chart will be plotted here~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~1 for solution, 1 for Issue~~~~~~~~~~~~~~~")
            bar_chart_for_solution_by_region(filtered_df, selected_region)
            bar_chart_for_issue_by_region(filtered_df, selected_region)
        elif graph_choice == 2:
            print("~~~~~~~~~~~~2 chart will be plotted here~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~1 for solution, 1 for Issue~~~~~~~~~~~~~~~")
            pie_chart_for_issue_by_region(filtered_df, selected_region)
            pie_chart_for_solution_by_region(filtered_df, selected_region)
        elif graph_choice == 3:
            print("~~~~~~~~~~~~2 chart will be plotted here~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~1 for solution, 1 for Issue~~~~~~~~~~~~~~~")
            line_graph_for_solution_by_region(filtered_df, selected_region)
            line_graph_for_issue_by_region(filtered_df, selected_region)
        elif graph_choice == 4:
            flag = True

    elif main_menu_choice == 4:
        graph_choice = graph()
        issue_days_dict, selected = avg_day_to_resolve_by_issue_type()
        if graph_choice == 1:
            bar_chart_avg_time_by_issue_type(issue_days_dict)
        elif graph_choice == 2:
            pie_chart_avg_time_by_issue_type(issue_days_dict)
        elif graph_choice == 3:
            line_graph_avg_time_by_issue_type(issue_days_dict)
        elif graph_choice == 4:
            flag = True

    elif main_menu_choice == 5:
        issue_dict = issue_counter()
        graph_choice = graph()
        if graph_choice == 1:
            bar_chart_for_issue(issue_dict)
        elif graph_choice == 2:
           pie_chart_for_issue(issue_dict)
        elif graph_choice == 3:
            line_graph_for_issue(issue_dict)
        elif graph_choice == 4:
            flag = True

    elif main_menu_choice == 6:
        solution_dict = solution_counter()
        graph_choice = graph()
        if graph_choice == 1:
            bar_chart_for_solution(solution_dict)
        elif graph_choice == 2:
           pie_chart_for_solution(solution_dict)
        elif graph_choice == 3:
            line_graph_for_solution(solution_dict)
        elif graph_choice == 4:
            flag = True
    elif main_menu_choice == 7:
        print("####################################################")
        print("~~~~~~~~~~~~~~~~~~~Thanks for Using Botes Parcels CRM System ~~~~~~~~~~~~~~~~~~~~#")
        print("####################################################")
        exit()
                
            
                
