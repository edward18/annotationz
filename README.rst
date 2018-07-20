Annotationz Module Repository
========================

This project is intendet to annotate data according to the ALKIS Ontology.

Additionally it is desired for the tool to be generic.


Getting Started
---------------
Given that 'ontology.owl' and 'data.xml' directories are known:
1. Importing the ontology with a preferred prefix. For alkis it would be **alk**.
2. Importing the data to transform.
3. Getting the desired elements from the data.xml.
4. Looping through the elements and transforming them.
5. Outputting the transformed data to console or file:

	a = Annotation()
	a.importOntology("ontology.owl", "ontologyPrefix")
	a.importData("data.xml")

	elements = a.getElementsByTagName("elementName", "parentName")
	for element in elements:
		a.annotate(element)

	a.output()