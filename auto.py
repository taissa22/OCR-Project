f = open("results.md", "a")
for i in range(38, 51):
    f = open("results.md", "a")
    f.write(f"""\
\n\n
### Teste {i}
      
#### DocTR
!['teste{i}'](./new_results/images/Figure_{i}.png)
!['teste{i}'](./new_results/images2/Figure_{i}.png)
#### Google Cloud Vision API
!['teste{i}'](./google_api/result_api{i}.png)
""")