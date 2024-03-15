from classification import ImageClassification

if __name__ == "__main__":
    classifier = ImageClassification()
    selected_directory = classifier.select_directory()
    filenames = classifier.get_files_names(selected_directory)
    classifier.classify_and_save_results(selected_directory, filenames)
