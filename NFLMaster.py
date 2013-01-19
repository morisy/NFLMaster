import urllib, datetime, re, csv, pprint
from datetime import datetime, timedelta

#
fetchedplays = 70 #how many plays to check
pp = pprint.PrettyPrinter(indent=4)


csvfile=open('nflplays.csv','ab') #this is the excel-compatible file that the data is piped to.



print "Important caveat: I'm only checking the first " + str(fetchedplays) + " plays." 
for play in playlist:
    try:
        url = 'http://itknowledgeexchange.techtarget.com' + blogurl + 'xmlrpc.php'
        blog = pyblog.WordPress(url, 'admin', pwd)
        posts = blog.get_recent_posts(numposts = fetchedposts)

        last_month_posts = [
            p for p in posts
                if prev_month_start <= datetime.strptime(str(p['dateCreated']), '%Y%m%dT%H:%M:%S').date() < this_month_start]
        last_month_approved_comment_count = 0
        #for p in posts:
        #    last_month_approved_comment_count = last_month_approved_comment_count + blog.get_comment_count(postid = p)['approved']
         # need to go in and re-add comment counts. Low priority.
        print "number of last month's posts at " + blogurl + ":", len(last_month_posts)
        print "number of approved comments for last month's " + str(blogurl) +" pages:",
        print last_month_approved_comment_count
        csvout.writerow([blogurl, len(last_month_posts), last_month_approved_comment_count])

    except pyblog.BlogError:
        print "Oops! The blog at " + blogurl + " is not configured properly."
        csvout.writerow([blogurl, "Error!", "Error!"])
                        

csvfile.close()
