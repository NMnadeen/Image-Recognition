from transformers import AutoProcessor

# Processor bruges kun til efterbehandling
processor = AutoProcessor.from_pretrained("microsoft/kosmos-2-patch14-224")

def label_return(generated_text): #Returnerer labels og responstekst

    responsTekst, entities = processor.post_process_generation(generated_text)

    labels = []
    for entity in entities:
        labels.append(entity[0])

    # Altid kun 4 labels
    while len(labels) < 4:
        labels.append(None)

    label1 = labels[0]
    label2 = labels[1]
    label3 = labels[2]
    label4 = labels[3]

    return responsTekst, label1, label2, label3, label4

# Pseudokode

'''
FUNKTION label_return(generated_text)

    Udfør processering af responstekst og entities
    
    OPRET tom list labels
    FOR entity i entities
        Tilføj entities til listen labels

    WHILE antallet af labels er mindre end 4
        Tilføj ingen elementer til listen labels

    Tildel
    label 1 = labels[0]
    label 2 = labels[1]
    label 3 = labels[2]
    label 4 = labels[3]

    Returnér responstekst, label1, label2, label3 og label4 
'''