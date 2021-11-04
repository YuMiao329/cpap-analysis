import json


def cal_avg_seal(text):
    """Calculate the average seal from the given strings of seals

    Using basic summation and division to calculate the average value
    of a given array. However, the array needs to be transformed from
    string to float type first before calculation

    :param text: string containing the array of seals separated by ","

    :returns: list of array with float type number
    """
    split_num = text.split(",")
    map_obj = map(float, split_num)
    list_of_integers = list(map_obj)
    return sum(list_of_integers) / len(list_of_integers)


def cal_avg_events(text):
    """Calculate the average events from the given strings of events

    Using basic summation and division to calculate the average value
    of a given array. However, the array needs to be transformed from
    string to float type first before calculation

    :param text: string containing the array of events separated by ","

    :returns: list of array with float type number
    """
    split_num = text.split(",")
    map_obj = map(float, split_num)
    list_of_integers = list(map_obj)
    return sum(list_of_integers) / len(list_of_integers)


def diagnosis(O2, avg_events):
    """Generate four types of reports based on O2 level and average of events

    From the results of the Events and O2 data, assign one of the following
    diagnoses to the patient:

    "normal sleep" if all O2 saturation values are 93 or higher and the
    average number of events per hour for the entire night is 5.0 or less.
    "hypoxia" if any of the O2 saturation values is below 93 and the
    average number of events per hour for the entire night is 5.0 or less
    "apnea" if all O2 saturation values are 93 or higher and the average
    number of events per hour for the entire night is greater than 5.0
    "hypoxia apnea" if any of the O2 saturation values is below 93 and
    the average number of events per hour for the entire night is
    greater than 5.0.

    :param O2: string containing the array of O2 level separated by ","
    :param avg_events: float type number stating the average events
    calculated by ca_avg_events function

    :returns: one of the four types of diagnosis
    "Normal Sleep", "Hypoxia", "Apnea" and "Hypoxia Apnea"
    """
    split_O2 = O2.split(",")
    map_O2 = map(float, split_O2)
    list_of_O2 = list(map_O2)
    hypoxia_check = False
    for O2_value in list_of_O2:
        if O2_value < 93:
            hypoxia_check = True
    if hypoxia_check and avg_events <= 5.0:
        return "Hypoxia"
    elif hypoxia_check and avg_events > 5.0:
        return "Hypoxia Apnea"
    if ~hypoxia_check and avg_events <= 5.0:
        return "Normal Sleep"
    if ~hypoxia_check and avg_events > 5.0:
        return "Apnea"


def output_json(dictionary):
    """Put each patient's information into a JSON file

    Feed in the basic dictionary from the modified list of
    dictionary. It will generate each person's basic information
    and will output JSON file containing that person's basic
    information such as First name, Last name, Hours, Seal,
    Events, O2,  Seal Average and Diagnosis. The name of
    the JSON file will be the form of First name-Last name.JSON

    :param dictionary: The basic information of each patient and
    it is in the form of python dictionary
    :return: Generate the JSON file in the current directory
    """
    name = dictionary["Name"].replace(" ", "-")
    filename = name + ".json"
    out_file = open(filename, 'w')

    first_name, last_name = dictionary["Name"].split()

    split_seal = dictionary["Seal"].split(",")
    map_seal = map(float, split_seal)
    list_of_seal = list(map_seal)

    split_events = dictionary["Events"].split(",")
    map_events = map(int, split_events)
    list_of_events = list(map_events)

    split_O2 = dictionary["O2"].split(",")
    map_O2 = map(int, split_O2)
    list_of_O2 = list(map_O2)

    output_dictionary = {"First Name": first_name,
                         "Last Name": last_name,
                         "Hours": float(dictionary["Hours"]),
                         "Seal": list_of_seal,
                         "Events": list_of_events,
                         "O2": list_of_O2,
                         "Seal Average": dictionary["Seal Average"],
                         "Diagnosis": dictionary["Diagnosis"]}
    json.dump(output_dictionary, out_file)
    out_file.close()


def CPAP_application():
    """The main execution function to generate report

    Obstructive sleep apnea is a condition in which
    breathing stops involuntarily for brief periods
    of time during sleep. The flow of air stops because
    the airways may constrict due to "floppy" muscles
    that do not keep the airways open. This disruption of
    airflow can lead to periods of decreased oxygen supply
    to the brain and other parts of the body, as well as
    poor sleep quality leading to daytime drowsiness.
    (https://www.healthline.com/health/sleep/obstructive-sleep-apnea)

    Obstructive sleep apnea is often treated with the
    use of a continuous positive airway pressure (CPAP)
    machine. The patient wears a mask connected to the
    CPAP. The mask provides pressurized air for the
    patient to breath. The pressure is set high enough
    to help keep open the airways so that they cannot
    collapse and block air flow. Breathing is not interrupted.

    """
    lines = []

    individual_lines = 5
    keys = ["Name", "Hours", "Seal", "Events", "O2",
            "Seal Average", "Events Average", "Diagnosis"]
    with open('sample_data.txt') as f:
        lines = f.readlines()
        lines = lines[:-1]
        num_lines = len(lines)
        num_ppl = int(num_lines / individual_lines)
        names = lines[0::5]
        hours = lines[1::5]
        seal = lines[2::5]
        events = lines[3::5]
        O2 = lines[4::5]

        avg_seal = seal[:]
        avg_events = events[:]
        result = lines[:]

        for i in range(num_ppl):
            names[i] = names[i][:-1]
            hours[i] = hours[i][:-1]
            seal[i] = seal[i][5:-1]
            events[i] = events[i][7:-1]
            O2[i] = O2[i][3:-1]

            avg_seal[i] = cal_avg_seal(seal[i])
            avg_events[i] = cal_avg_events(events[i])
            result[i] = diagnosis(O2[i], avg_events[i])

    dic = {}
    total_list = []
    for i in range(num_ppl):
        dic = {keys[0]: names[i],
               keys[1]: hours[i],
               keys[2]: seal[i],
               keys[3]: events[i],
               keys[4]: O2[i],
               keys[5]: avg_seal[i],
               keys[6]: avg_events[i],
               keys[7]: result[i]
               }
        total_list.append(dic)

    print(total_list)
    for people in total_list:
        output_json(people)


if __name__ == "__main__":
    CPAP_application()
