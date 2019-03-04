# 3M101-Quadtree

 OUTILS :
 - LaTeX :
   - présentation de bibtex : https://fr.wikipedia.org/wiki/BibTeX, https://www.tuteurs.ens.fr/logiciels/latex/bibtex.html
   - génération du bibtex pour un article wikipedia : https://irl.github.io/bibwiki/
   - divers docs sur LaTeX http://www.edu.upmc.fr/c2i/ressources/latex/, https://fr.wikibooks.org/wiki/LaTeX/Structuration_du_texte
   - créer des arbres binaires en latex : https://github.com/MartinThoma/LaTeX-examples/tree/master/tikz/binary-tree
   - création de latex à partir de python : https://jeltef.github.io/PyLaTeX/current/examples/tikzdraw.html
- Arbres Binaires :
  - Arbres, arbre d'expression, arbre binaire de recherche : http://pageperso.lif.univ-mrs.fr/~francois.denis/algoMPCI/chap1.pdf
  - Convention de style pour Python : https://www.python.org/dev/peps/pep-0008/
  - implémentation d'arbre binaires en python : https://www.laurentluce.com/posts/binary-search-tree-library-in-python/
  https://stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree
  https://stackoverflow.com/questions/5444394/how-to-implement-a-binary-search-tree-in-python
  - biblothèque d'arbre binaire :
  https://pypi.org/project/binarytree/, https://pypi.org/project/bintrees/, https://github.com/TylerSandman/py-bst 

TODO :
- Description et vocabulaire arbres binaires (Charlotte)
- Arbre d'expression (optionnel)
- Arbres binaires de recherche : affichage (parcours infixe/suffixe/préfixe) / insertion (Charlotte) / suppression (Thiziri) / recherche / modification (Thiziri) : étude théorique (algo en pseudo code / python + compléxité)
- comparaison implémentation : liste VS structure récursive (Serge)
- Implémenter un arbre binaire de recherche : cas concret (Thiziri)
- générateur d'arbre alétoire (Kevin)
- étude expérimentale de la complexité (Kevin) /// Problème avec Python -> C
    éventuellement faire des tests sur des biblothèques déjà faites :
    https://pypi.org/project/binarytree/, https://pypi.org/project/bintrees/, https://github.com/TylerSandman/py-bst par ex. 
- idem Quadtree
- Implémenter annales s1 2017 (Serge)
- Implémentation de rotation pour les BST + utilisation dans l'insertion pour garder des arbres équilibrés.
- regarder si un concept de rotation peut être appliqué pour les quadtree.
- implémenter une fonction "equals" ?
- implémenter rotation + insertion avec rotation
- implémenter une fonction "hauteur min" (calcul du chemin racine -> feuille de taille minimal) + une fonction calculant un coeff d'équilibrage (|hauteur - hauteur_min|)
- faire des tests expérimentaux sur des arbres créé aléatoirement à partir d'une même liste (ordonnée différemment). Comparer les fonctions insertion et insertions classiques.

- idées de trucs supplémentaire à chercher, sur la théorie : 
    - Nombre d'arbre binaire pour une taille n donnée ? (indice : nombres de catalan, mais ça marche que pour les arbres binaires entiers). 
    - Nombre d'arbre binaire de recherche pour une taille n donnée ? 
    - Même question pour les quadtree.
    - questions sur les hauteurs : espérance de la hauteur en fonction de la taille ? Variance ?
    


