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