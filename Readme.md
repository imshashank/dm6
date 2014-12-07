Data Mining Project for CSE OSU CLass
===========
By
Shashank Agarwal (agarwal.202@osu.edu)
Anurag Kalra (kalra.25@osu.edu)

all code is in the code6 folder and reports are in the report6 folder in pdf and docx format

##Instructions

###We created a the transactional vector which is in the file 'docs.txt'. 
===========================================================================================================================

Part 1:

Procedure:
1) Create assosiation rules for all (or split 80-20) documents in files "docs.txt" and labels.txt using apriori 
	command: ./apriori -s5 -c80  -tr -R labels.txt docs_80.txt output.txt
	Final file-> output.txt

2) Iterate over various values of support (-s) and confidence (-c)

3) Use classification rules to predict files and check accuracy
	commnd: sudo python test.py output.txt docs_20.txt res.txt
	Final File->res.txt

4) Do above for 60-40 split

===========================================================================================================================

Part 2:

Procedure
1) Create feature_vector for the docs file "feature_matrix.pytext"
2) Use the feature vector to cluster (k=8,k=16)
	command: kmeans.py 8 

3) Create separate document & labels files for each cluster
	output -> files from range 0.txt to k.txt
			labels from 0_labels to k_labels.txt

4) Split and run apriori on each file
 	command:	./apriori -s3 -c50 -m2 -tr -R labels.txt docs.txt output.txt
 	final_file-> output.txt

5) Use classification rules to predict files and check accuracy
	commnd: python test.py output.txt 0.txt res.txt
	Final File->res.txt



A simple way to do all above is to use the below comman
	command: python shell.py docs.txt labels.txt 60 3 50
	here 60 is the split (60-40) 
	3 is the support
	50 is the confidence


The files from 8 means where (k=8) are provided in file 0 to k.txt and labels from 0 to k_labels.txt
===========================================================================================================================
Executing the Code:

To run apriori on docs.txt & labels.txt enter:

	make apr

	#deafault values:  -s3 -c50


To get the accuracy run:
	make accuracy


To split and run tests run

	make shell 

The results are saved in results.txt file

This runs the following command:

	python shell.py docs.txt labels.txt 60 3 50
		here 60 is the split
		3 is the support
		50 is the confidence


===========================================================================================================================
Contributions:
Shashank Agarwal & Anurag Kalra both implemented the "apriori" classification rules generation and testing scripts. The work overlaps and is hard to be segregated.

P.S: The kmeans file have not been included as the feature matrix was very large and kmeans required a lot of files that have been submitted in previous projects.







