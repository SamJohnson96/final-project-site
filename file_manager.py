class FileManager:

    def get_text_file(self,name):
        with open(name, 'r') as myfile:
            file_content=myfile.read().replace('\n', '')
        return file_content
