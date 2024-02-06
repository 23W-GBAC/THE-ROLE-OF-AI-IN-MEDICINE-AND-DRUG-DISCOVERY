import json

def load_data():
    try:
        with open('patients.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def save_data(data):
    with open('patients.json', 'w') as file:
        json.dump(data, file, indent=2)

def register_patient():
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    gender = input("Enter patient's gender: ")
    
    patient = {
        'name': name,
        'age': age,
        'gender': gender,
        'prescriptions': []  # Initialize prescriptions as an empty list
    }
    
    data = load_data()
    data.append(patient)
    save_data(data)
    print(f"Patient {name} registered successfully!")

def prescribe_medicine(patient):
    medicine = input("Enter prescribed medicine: ")
    dosage = input("Enter dosage: ")
    
    prescription = {
        'medicine': medicine,
        'dosage': dosage
    }
    
    patient['prescriptions'].append(prescription)
    save_data(data)
    print(f"Prescription added for {patient['name']}: {medicine} - {dosage}")

def display_prescriptions(patient):
    prescriptions = patient['prescriptions']
    
    if not prescriptions:
        print(f"No prescriptions for {patient['name']} yet.")
    else:
        print(f"\nPrescriptions for {patient['name']}:")
        for idx, prescription in enumerate(prescriptions, start=1):
            print(f"{idx}. Medicine: {prescription['medicine']}, Dosage: {prescription['dosage']}")
        print()

def main():
    while True:
        print("\nHealthcare Automation System")
        print("1. Register Patient")
        print("2. Prescribe Medicine")
        print("3. Display Prescriptions")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            register_patient()
        elif choice == '2':
            patient_id = int(input("Enter patient ID: "))
            if 1 <= patient_id <= len(data):
                prescribe_medicine(data[patient_id - 1])
            else:
                print("Invalid patient ID. Please enter a valid ID.")
        elif choice == '3':
            patient_id = int(input("Enter patient ID: "))
            if 1 <= patient_id <= len(data):
                display_prescriptions(data[patient_id - 1])
            else:
                print("Invalid patient ID. Please enter a valid ID.")
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    data = load_data()  # Load patient data at the beginning
    main()
