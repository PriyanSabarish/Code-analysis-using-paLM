import pprint
import google.generativeai as palm
import os
palm.configure(api_key='AIzaSyCP0mlpy_DhFZGm08cQbALkNINW-CStAqg')



def analyze_code(code,pr):
    prompt= code + "\n" + pr
    return prompt

def drop_file():
  file_path = "D:/fprojects/social-app/phobapp/lib/pages/home_page.dart"
  with open(file_path, "r") as f:
    file_contents = f.read()
  f.close()

  return file_contents


directory_path = "D:/fprojects/social-app/phobapp/lib/pages"
files= os.listdir(directory_path)

for i, file in enumerate(files, start=1):
    print(f"{i}. {file}")


'''models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print("Files in the directory:")
code = drop_file()
pr = "Count the number of functions and name them"
prompt=analyze_code(code,pr)
completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)
print(completion.result)

'''