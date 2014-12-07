import subprocess
import sys
docs_file =sys.argv[1]
labels_file=sys.argv[2]
rules_file = "rules.txt"
out_file="result.txt"
support =sys.argv[4]
confidence = sys.argv[5]

divide = sys.argv[3]
# 20 lines per file
outputBase = 'output_'+docs_file+"_" # output.1.txt, output.2.txt, etc.

# This is shorthand and not friendly with memory
# on very large files (Sean Cavanagh), but it works.
input = open(docs_file, 'r').read().split('\n')

var=  float(divide)/100
splitLen = int(len(input)*var)
print splitLen

at = 1
for lines in range(0, len(input), splitLen):
    # First, get the list slice
    outputData = input[lines:lines+splitLen]

    # Now open the output file, join the new slice with newlines
    # and write it out. Then close the file.
    output = open(outputBase + str(at) + '.txt', 'w')
    output.write('\n'.join(outputData))
    output.close()

    # Increment the counter
    at += 1

#train output_file_1.txt
#test output_file_2.txt
#./apriori -s3 -c50 -m2 -tr -R labels.txt output_file_1.txt results.txt
print "sudo ./apriori -s"+support+" -c"+confidence+" -m2 -tr -R "+labels_file +" output_"+docs_file+"_1.txt rules_"+docs_file+".txt +\n"
print "sudo python test.py rules_"+docs_file +".txt output_"+docs_file+"_2.txt results.txt +\n"

command = " ./apriori -s"+support+" -c"+confidence+" -m2 -tr -R "+labels_file +" output_"+docs_file+"_1.txt rules_"+docs_file+".txt | sleep 10s | python test.py rules_"+docs_file +".txt output_"+docs_file+"_2.txt results.txt"

#command = "sudo ./apriori -s3 -c50 -m2 -tr -R labels.txt output_file_1.txt output.txt | sudo python test.py output.txt output_file_2.txt results.txt"

#ps = subprocess.Popen(['sudo','./apriori','-s3'. '-c50','-m2','-t','-R','labels.txt' ,'output_file_1.txt','output.txt', '--columns', '1000'],shell=True, stdout=subprocess.PIPE)


ps = subprocess.Popen([command,'--columns', '1000'],shell=True, stdout=subprocess.PIPE)


#sudo python test.py out.txt docs.txt output.txt

#command = "python test.py output.txt output_file_2.txt results.txt"

#ps = subprocess.Popen([command,'--columns', '1000'],shell=True, stdout=subprocess.PIPE)
output = ps.communicate()[0]
for line in output.splitlines():
    if 'rtptransmit' in line:
        print(line)
