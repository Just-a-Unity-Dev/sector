from glob import glob
import pyfiglet
import time

exclude = ["README.md"]

def main():
    pyfiglet.print_figlet("Indexer")

    start = time.process_time()

    print("now indexing files.")
    files = glob("**/*.md", recursive=True)
    print("indexed files.")

    print("now writing files.")

    with open("page_index.md", "w") as file:
        file.truncate(0) # reset it
        file.write("# Page Index\n\n")
        file.write("*if there is an issue, please submit a [bug report](https://github.com/Just-a-Unity-Dev/sector/issues/new/choose)*\n\n")
        category = None
        file.write("## Meta\n\n")
        for markdown in files:
            if markdown.startswith("build") or markdown in exclude:
                continue
                
            split = markdown.replace("\\", "/").split("/")
            name = split.pop()[:-3].split("_")

            for i,item in enumerate(name):
                name[i] = item.capitalize()
            
            name = ' '.join(name)

            if len(split) > 0:
                if category != split[0]:
                    file.write(f"\n## {split[0].capitalize()}\n\n")
                    category = split[0]
            
            if len(split) > 1:
                name += f" ({split[1]})"
            
            if name == "Index":
                name = "Homepage"

            file.write(f"- [{name}]({markdown[:len(markdown) - 3]})\n")
            
    end = time.process_time()

    print(f"finished in {(end - start) * 10**3}ms.")

if __name__ == "__main__":
    main()