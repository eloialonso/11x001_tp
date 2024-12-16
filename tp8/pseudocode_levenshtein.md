**Pseudocode** : 

```
entier levenshtein(str a, str b):
   
    Initialiser D, une matrice d'entiers de taille (len(a) + 1) x (len(b) + 1), remplie de 0.
    
    Pour i de 1 à len(a) + 1:
        D[i][0] = i

    Pour j de 1 à len(b) + 1:
        D[0][j] = j
    
    Pour i de 1 à len(a) + 1:
        Pour j de 1 à len(b) + 1:
            Si 
                a[i - 1] == b[j - 1]
            Alors 
                D[i][j] = D[i - 1][j - 1]
            Sinon 
                D[i][j] = min(
                    D[i - 1][j] + 1,        // suppression
                    D[i][j - 1] + 1,        // insertion
                    D[i - 1][j - 1] + 1     // remplacement
                ) 
  
    Retourner D[len(a)][len(b)]
```
