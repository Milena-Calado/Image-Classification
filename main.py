"""This is the main project file. where the ImageClassification class is called to execute the code."""

from ImageClassification import ImageClassification

if __name__ == "__main__":

    """Classify the images in the selected directory and save the results to a CSV file."""

    classifier = ImageClassification()
    selected_directory = classifier.select_directory()
    filenames = classifier.get_files_names(selected_directory)
    classifier.classify_and_save_results(selected_directory, filenames)
