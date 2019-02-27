# 3M101-Quadtree
Docs divers :
Arbres, arbre d'expression, arbre binaire de recherche http://pageperso.lif.univ-mrs.fr/~francois.denis/algoMPCI/chap1.pdf
Convention de style pour Python : https://www.python.org/dev/peps/pep-0008/
écriture en LaTeX : https://fr.wikibooks.org/wiki/LaTeX/Structuration_du_texte



- Description et vocabulaire arbres binaires (Charlotte)
- Arbre d'expression (optionnel)
- Arbres binaires de recherche : affichage (parcours infixe/suffixe/préfixe) / insertion (Charlotte) / suppression (Thiziri) / recherche / modification (Thiziri) : étude théorique (algo en pseudo code / python + compléxité)
- comparaison implémentation : liste VS structure récursive (Serge)
- Apprendre à créer des arbres en LaTeX (Serge) 
    ok cf https://github.com/MartinThoma/LaTeX-examples/tree/master/tikz/binary-tree
- Implémenter un arbre binaire de recherche : cas concret (Thiziri)
- générateur d'arbre alétoire (Kevin)
- étude expérimentale de la complexité (Kevin) /// Problème avec Python -> C
    éventuellement faire des tests sur des biblothèques déjà faites :
    https://pypi.org/project/binarytree/, https://pypi.org/project/bintrees/, https://github.com/TylerSandman/py-bst par ex. 
- idem Quadtree
- Implémenter annales s1 2017 (Serge)
- Implémentation de rotation pour les BST + utilisation dans l'insertion pour garder des arbres équilibrés.
- regarder si un concept de rotation peut être appliqué pour les quadtree.
- à voir pour la génération du code LaTeX d'arbre : https://jeltef.github.io/PyLaTeX/current/examples/tikzdraw.html
- implémenter une fonction "equals" ?
- implémenter rotation + insertion avec rotation
- implémenter une fonction "hauteur min" (calcul du chemin racine -> feuille de taille minimal) + une fonction calculant un coeff d'équilibrage (|hauteur - hauteur_min|)
- faire des tests expérimentaux sur des arbres créé aléatoirement à partir d'une même liste (ordonnée différemment). Comparer les fonctions insertion et insertions classiques.

- idées de trucs supplémentaire à chercher, sur la théorie : 
    - Nombre d'arbre binaire pour une taille n donnée ? (indice : nombres de catalan, mais ça marche que pour les arbres binaires entiers). 
    - Nombre d'arbre binaire de recherche pour une taille n donnée ? 
    - Même question pour les quadtree.
    - questions sur les hauteurs : espérance de la hauteur en fonction de la taille ? Variance ?
    
 

Source pour l'implémentation en python :

https://www.laurentluce.com/posts/binary-search-tree-library-in-python/
https://stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree
https://stackoverflow.com/questions/5444394/how-to-implement-a-binary-search-tree-in-python
