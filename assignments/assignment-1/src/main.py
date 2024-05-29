import os
import spacy
import pandas as pd
from codecarbon import EmissionsTracker


def main():
    tracker = EmissionsTracker(project_name=f"a1_emissions", 
        experiment_id=f"a1_emissions",
        output_dir=os.path.join("out","emissions"),
        output_file=f"a1_emissions.csv")
    tracker.start()

    tracker.start_task("a1_main")
    nlp = spacy.load("en_core_web_md")

    data_path = os.path.join("in", "USEcorpus")
    dirs = sorted(os.listdir(data_path))

    for directory in dirs:
        subfolder = data_path +"/"+ directory
        filenames = (sorted(os.listdir(subfolder)))
        folder_info = []

        for text_file in filenames:
            path = (subfolder +"/"+ text_file)
            # open it
            with open(path, encoding = "latin-1") as f: text = f.read()
            # add text files to doc
            doc = nlp(text)
            # create counters
            noun_count = 0
            verb_count = 0
            adj_count = 0
            adv_count = 0

            # for loop: add 1 to counter
            for token in doc:
                if token.pos_ == "NOUN":
                    noun_count += 1
                elif token.pos_ == "VERB":
                    verb_count += 1
                elif token.pos_ == "ADJ":
                    adj_count += 1
                elif token.pos_ == "ADV":
                    adv_count += 1

            # relative frequencies
            relative_freq_noun = round((noun_count/len(doc)) * 10000, 2)
            relative_freq_verb = round((verb_count/len(doc)) * 10000, 2)
            relative_freq_adj = round((adj_count/len(doc)) * 10000, 2)
            relative_freq_adv = round((adv_count/len(doc)) * 10000, 2)

            # extracting PER, LOC, ORGS
            persons = set()
            for ent in doc.ents:
                    if ent.label_ == 'PERSON':
                        persons.add(ent.text)
            num_persons = len(persons)

            locations = set()
            for ent in doc.ents:
                    if ent.label_ == 'LOC':
                        locations.add(ent.text)
            num_locations = len(locations)

            organisations = set()
            for ent in doc.ents:
                    if ent.label_ == 'ORGS':
                        organisations.add(ent.text)
            num_organisations = len(organisations)

            file_info = [text_file, relative_freq_noun, relative_freq_verb, relative_freq_adj, relative_freq_adv, num_persons, num_locations, num_organisations]

            folder_info.append(file_info)

            df = pd.DataFrame(folder_info, 
                        columns=["Filename", "RelFreq Noun", "RelFreq VERB", "RelFreq ADJ", "RelFreq ADV", "Unique PER", "Unique LOC", "Unique ORGS"])

            outpath = os.path.join("out", directory + ".csv")
            df.to_csv(outpath)
    tracker.stop_task()
    tracker.stop()

if __name__=="__main__":
    main()
