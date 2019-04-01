# 3M101-Quadtree

 OUTILS :
 
 - LaTeX :
   - Lien overleaf : https://fr.overleaf.com/project/5c88fbf71448113af5bddde5
   - présentation de bibtex : https://fr.wikipedia.org/wiki/BibTeX, https://www.tuteurs.ens.fr/logiciels/latex/bibtex.html
   - tip sur bibtex : souvent le code bib est déjà dispo, pas besoin de le réécrire, il faut chercher le nom de la référence + Bibtex sur google. Par exemple pour Introduction To Algorithms de Cormen & al. : https://dl.acm.org/citation.cfm?id=1614191 puis cliquer sur Bibtex dans "export format".
   - pour l'insertion du fichier bib : \bibliography{../../biblio} à mettre en haut de votre doc .TeX chaque "../" correspondant au niveau dans l'arborescence des dossiers. le .bib est à la racine, si le .TeX est dans un sous dossier il faut mettre qu'un "../"
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
  
- Quadtree :
  - https://kpully.github.io/Quadtrees/
  - https://fr.wikipedia.org/wiki/Quadtree
  - http://www.astroml.org/book_figures/chapter2/fig_quadtree_example.html7
  - Application :
    - compression de données et dataviz https://www.phase2technology.com/blog/using-d3-quadtrees-power-interactive-map-bonnier-corporation
    - détetection de collision : https://stackoverflow.com/questions/41946007/efficient-and-well-explained-implementation-of-a-quadtree-for-2d-collision-det video : https://streamable.com/3pgmn
    - traitement d'image (compression) : https://www.michaelfogleman.com/static/quads/ source : https://github.com/fogleman/Quads
    
  
  
- Mesures expérimentales :
  - https://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly pour la régression logarithmique. L'idée est de faire une régression polynomiale sur log(x) comme suggéré par M. Thierry

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
- chercher applications quadtree region vs quadtree point
- implémenter visualisation de quadtree region
- un quadtree de hauteur n = image de taille ?? (n x n) ou (2

- idées de trucs supplémentaire à chercher, sur la théorie : 
    - Nombre d'arbre binaire pour une taille n donnée ? (indice : nombres de catalan, mais ça marche que pour les arbres binaires entiers). 
    - Nombre d'arbre binaire de recherche pour une taille n donnée ? 
    - Même question pour les quadtree.
    - questions sur les hauteurs : espérance de la hauteur en fonction de la taille ? Variance ? https://cs.stackexchange.com/questions/96448/average-height-of-a-bst-with-n-nodes
    


