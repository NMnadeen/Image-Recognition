import requests

from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq


model = AutoModelForVision2Seq.from_pretrained("microsoft/kosmos-2-patch14-224")
processor = AutoProcessor.from_pretrained("microsoft/kosmos-2-patch14-224")

def process_image(image_path):

    prompt = "<grounding>An image of" # Tekst den skal starte med i responstekst. 
    
    image = Image.open(image_path) # Åbn billede fra den givne url

    #Gem og genindlæs billedet, for at sikre korrekt type/format
    image.save("new_image.jpg") 
    image = Image.open("new_image.jpg") 

    
    inputs = processor(text=prompt, images=image, return_tensors="pt") # Forbered input til AI-modellen dvs. tekst og billede.
    # Processoren tager teksten, som laves om til token id'er
    # Billedet laves om til pixelværdier
    # Alt laves til sidst om til tensorer som modellen skal have som input


    generated_ids = model.generate( #Modellens keys i dens dictionary(input) tildeles nogle værdier som anvendes til at generere tekst og labels
        
        pixel_values=inputs["pixel_values"], #Hver pixel får en værdi som modellen arbejder med 
        input_ids=inputs["input_ids"], # Laver start-promptet om til tokens, så modellen ved hvad for noget tekst der skal genereres
        attention_mask=inputs["attention_mask"], #Den filtrerer hvilke tokens der kan, og ikke kan bruges
        image_embeds=None, #Billede-embedding anvendes ikke, og sættes derfor til none
        image_embeds_position_mask=inputs["image_embeds_position_mask"], 
        use_cache=True, #Gemmer beregninger for effektivitet
        max_new_tokens=128, #Maksimal mængde af tokens, modellen må generere
    )
    
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0] # Konverterer modellens output til tekst der kan læses

    return generated_text #Returnerer responstekst og labels

#print(inputs) = dictionary


# Prosakode til LabelReturn
'''
FUNKTION Process_image
    Begyndelsesteksten bestemmes
    Billede åbnes og genindlæses
    Tekst og billede laves om til datatyper der er kompatible med modellen
    Modellen behandler billedet og genererer beskrivende tekst 
'''

'''
# Specify `cleanup_and_extract=False` in order to see the raw model generation.
processed_text = processor.post_process_generation(generated_text, cleanup_and_extract=False)

print(processed_text)
# `<grounding> An image of<phrase> a snowman</phrase><object><patch_index_0044><patch_index_0863></object> warming himself by<phrase> a fire</phrase><object><patch_index_0005><patch_index_0911></object>.`

# By default, the generated  text is cleanup and the entities are extracted.
processed_text, entities = processor.post_process_generation(generated_text)

print(processed_text)
# `An image of a snowman warming himself by a fire.`

print(entities)
# `[('a snowman', (12, 21), [(0.390625, 0.046875, 0.984375, 0.828125)]), ('a fire', (41, 47), [(0.171875, 0.015625, 0.484375, 0.890625)])]`
'''