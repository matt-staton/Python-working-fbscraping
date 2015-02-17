__author__ = 'Vicky'

# reference: http://simplebeautifuldata.com/2014/08/25/simple-python-facebook-scraper-part-1/
import lib2to3
import urllib2
import json
import pandas




def main():
    list_companies = ['walmart', 'cisco', 'pepsi', 'facebook', 'generalmotors', 'chevrolet', 'cadillac',
                      'honda', 'ford']
    graph_url = 'http://graph.facebook.com/'
    list_json = []

    with open('D:\\Python\\facebook\\fb.json', 'w') as outfile: # r for reading, w for writing (overwriting!), a for appending
        # you can use open(name, 'a'); this will create the file if the file does not exist, but will not truncate the existing file.
        for company in list_companies:
            # make graph api with company username
            current_page = graph_url + company

            # open public page in facebook api  (the most important part really. should memorize it -- open, read, loads)
            web_response = urllib2.urlopen(current_page) # taking our URL string we created and storing the response
            readable_page = web_response.read() #  converts our response object into a readable 'html' like document that you can print to console
            json_fbpage = json.loads(readable_page) # taking our readable_page variable and converting it to a JSON object
            # This will allow us to refer to information within that original mess, by key value pairs, kind of like a Python dictionary.
            # json_fbpage is already a dict object at this time. If something goes wrong, check all object types again.
            list_json.append(json_fbpage) # if multiple json objects, you need to put them into a list first, and dump the whole list
            #print(json_fbpage)

        json.dump(list_json, outfile, indent=4)
        outfile.close()

        # read this new json file. from now on all operations are under 'r' mode
        with open(outfile.name, 'r') as infile: # outfile.name is used to solve the problem of 'need string or buffer, file found'
            json_test = json.load(infile)
            infile.seek(0)
            json_new = infile.read()

            # load and query this new json file
            json_new_query = json.loads(json_new)
            dict = {}
            for obj in json_new_query:
                dict['name'] = obj['username']
                dict['likes'] = obj['likes']




    outfile.close()

if __name__ == '__main__':
        main()
