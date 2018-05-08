

```python
# Dependencies
import tweepy
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Twitter API Keys
consumer_key = 'ncIYApS06S4k8VpBrqUYOk8wb'
consumer_secret = 'oR5HNsL6twBliSlTLojB8a63jcqh2WnfsCySZ9mzd64voAGrSA'
access_token = '25749595-JC72urBHJsrwxFHRMiRjvayKDJIHQvxbNwzNob6TT'
access_token_secret = '4pH5dgPAXzx3dMP5HMudZzDciv4iVnizYcFXGgT3HnaHQ'

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
```


```python
tweet_txt=[]
compound_tweet=[]
tweet_date=[]
retweet_cnt=[]
fvt_cnt=[]
for x in range(0, 150):
    public_tweets = api.user_timeline('tim_cook', page=x)
        
    for tweet in public_tweets:

            # Run Vader Analysis on each tweet
        results = analyzer.polarity_scores(tweet["text"])
        compound = results["compound"]
        date=tweet['created_at']
        txt=tweet['text']
        fvt=tweet['favorite_count']
        retweet=tweet['retweet_count']
            # saving values
        compound_tweet.append(compound)
        tweet_txt.append(txt)
        tweet_date.append(date)
        retweet_cnt.append(retweet)
        fvt_cnt.append(retweet)

```


```python
#creating dictionary 
results = {
    "Date":tweet_date,
    "Text":tweet_txt,
    "Retweet Count":retweet_cnt,
    "Favorite Count":fvt_cnt,
    "Compound": compound_tweet
}

tweets=pd.DataFrame(results)
tweets
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Compound</th>
      <th>Date</th>
      <th>Favorite Count</th>
      <th>Retweet Count</th>
      <th>Text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.8591</td>
      <td>Wed Apr 18 00:10:33 +0000 2018</td>
      <td>90</td>
      <td>90</td>
      <td>Throughout her life, Barbara Bush showed us al...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0000</td>
      <td>Mon Apr 09 22:57:32 +0000 2018</td>
      <td>17233</td>
      <td>17233</td>
      <td>Every Apple store, every data center, every Ap...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.3818</td>
      <td>Mon Apr 09 13:30:21 +0000 2018</td>
      <td>2266</td>
      <td>2266</td>
      <td>Thanks to Apple customers around the world for...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.8126</td>
      <td>Sat Apr 07 16:30:19 +0000 2018</td>
      <td>1196</td>
      <td>1196</td>
      <td>Our hearts go out to the victims in Münster an...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.6114</td>
      <td>Sat Apr 07 04:42:04 +0000 2018</td>
      <td>1125</td>
      <td>1125</td>
      <td>Apple loves Tokyo and our customers, employees...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.7096</td>
      <td>Wed Apr 04 20:30:56 +0000 2018</td>
      <td>354</td>
      <td>354</td>
      <td>Great visit @LawsonStateCC. Alabama’s @ACCS_Ed...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.4404</td>
      <td>Wed Apr 04 18:10:06 +0000 2018</td>
      <td>435</td>
      <td>435</td>
      <td>Full of hope this morning, hearing from hundre...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.8689</td>
      <td>Wed Apr 04 16:50:33 +0000 2018</td>
      <td>1269</td>
      <td>1269</td>
      <td>It’s an honor to be in Birmingham celebrating ...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.3862</td>
      <td>Tue Apr 03 21:52:26 +0000 2018</td>
      <td>7349</td>
      <td>7349</td>
      <td>From everyone at Apple, we send our sympathy a...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.9517</td>
      <td>Sun Apr 01 14:05:28 +0000 2018</td>
      <td>1384</td>
      <td>1384</td>
      <td>Wishing a #HappyEaster to people everywhere. M...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.4215</td>
      <td>Fri Mar 30 21:25:55 +0000 2018</td>
      <td>589</td>
      <td>589</td>
      <td>Chag Sameach to everyone around the world shar...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.8779</td>
      <td>Tue Mar 27 19:53:04 +0000 2018</td>
      <td>810</td>
      <td>810</td>
      <td>Thanks to the students and faculty of Lane Tec...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0.7500</td>
      <td>Tue Mar 27 12:46:22 +0000 2018</td>
      <td>2745</td>
      <td>2745</td>
      <td>Good morning, Chicago! We’re going back to sch...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0.1154</td>
      <td>Tue Mar 27 00:41:27 +0000 2018</td>
      <td>1410</td>
      <td>1410</td>
      <td>"In the field of public education the doctrine...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0.8858</td>
      <td>Mon Mar 26 00:24:16 +0000 2018</td>
      <td>600</td>
      <td>600</td>
      <td>Congratulations to @DukeMBB and Coach K on a t...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.4019</td>
      <td>Mon Mar 19 17:22:23 +0000 2018</td>
      <td>730</td>
      <td>730</td>
      <td>We stand with our Austin coworkers, friends an...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.8395</td>
      <td>Sat Mar 17 12:49:19 +0000 2018</td>
      <td>807</td>
      <td>807</td>
      <td>Happy #StPatricksDay to our team in Ireland an...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0.4234</td>
      <td>Wed Mar 14 12:58:16 +0000 2018</td>
      <td>9660</td>
      <td>9660</td>
      <td>“The greatest enemy of knowledge is not ignora...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.3818</td>
      <td>Thu Mar 08 14:01:10 +0000 2018</td>
      <td>3118</td>
      <td>3118</td>
      <td>“There are two powers in the world; one is the...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>0.9576</td>
      <td>Sat Mar 03 22:43:23 +0000 2018</td>
      <td>1020</td>
      <td>1020</td>
      <td>So proud of @AuburnMBB @coachbrucepearl on win...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0.8591</td>
      <td>Wed Apr 18 00:10:33 +0000 2018</td>
      <td>91</td>
      <td>91</td>
      <td>Throughout her life, Barbara Bush showed us al...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>0.0000</td>
      <td>Mon Apr 09 22:57:32 +0000 2018</td>
      <td>17233</td>
      <td>17233</td>
      <td>Every Apple store, every data center, every Ap...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>0.3818</td>
      <td>Mon Apr 09 13:30:21 +0000 2018</td>
      <td>2266</td>
      <td>2266</td>
      <td>Thanks to Apple customers around the world for...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>-0.8126</td>
      <td>Sat Apr 07 16:30:19 +0000 2018</td>
      <td>1196</td>
      <td>1196</td>
      <td>Our hearts go out to the victims in Münster an...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>0.6114</td>
      <td>Sat Apr 07 04:42:04 +0000 2018</td>
      <td>1125</td>
      <td>1125</td>
      <td>Apple loves Tokyo and our customers, employees...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>0.7096</td>
      <td>Wed Apr 04 20:30:56 +0000 2018</td>
      <td>354</td>
      <td>354</td>
      <td>Great visit @LawsonStateCC. Alabama’s @ACCS_Ed...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>0.4404</td>
      <td>Wed Apr 04 18:10:06 +0000 2018</td>
      <td>435</td>
      <td>435</td>
      <td>Full of hope this morning, hearing from hundre...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>0.8689</td>
      <td>Wed Apr 04 16:50:33 +0000 2018</td>
      <td>1269</td>
      <td>1269</td>
      <td>It’s an honor to be in Birmingham celebrating ...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>0.3862</td>
      <td>Tue Apr 03 21:52:26 +0000 2018</td>
      <td>7349</td>
      <td>7349</td>
      <td>From everyone at Apple, we send our sympathy a...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>0.9517</td>
      <td>Sun Apr 01 14:05:28 +0000 2018</td>
      <td>1384</td>
      <td>1384</td>
      <td>Wishing a #HappyEaster to people everywhere. M...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>527</th>
      <td>-0.0258</td>
      <td>Mon Jan 20 04:57:54 +0000 2014</td>
      <td>825</td>
      <td>825</td>
      <td>Remembering my lifelong hero. "Injustice anywh...</td>
    </tr>
    <tr>
      <th>528</th>
      <td>0.5562</td>
      <td>Fri Jan 17 04:52:03 +0000 2014</td>
      <td>1302</td>
      <td>1302</td>
      <td>Having fun in Beijing at the iPhone launch wit...</td>
    </tr>
    <tr>
      <th>529</th>
      <td>0.3612</td>
      <td>Thu Jan 16 03:34:22 +0000 2014</td>
      <td>992</td>
      <td>992</td>
      <td>If you haven't seen this, I'd recommend watchi...</td>
    </tr>
    <tr>
      <th>530</th>
      <td>0.8065</td>
      <td>Tue Jan 07 15:27:51 +0000 2014</td>
      <td>214</td>
      <td>214</td>
      <td>Congratulations to #FSU coaches, team, and fan...</td>
    </tr>
    <tr>
      <th>531</th>
      <td>0.8074</td>
      <td>Tue Jan 07 15:25:52 +0000 2014</td>
      <td>1506</td>
      <td>1506</td>
      <td>Shout out to @CoachGusMalzahn and the entire #...</td>
    </tr>
    <tr>
      <th>532</th>
      <td>0.8777</td>
      <td>Wed Jan 01 14:27:47 +0000 2014</td>
      <td>2094</td>
      <td>2094</td>
      <td>Happy New Year! Wishing everyone their best ye...</td>
    </tr>
    <tr>
      <th>533</th>
      <td>0.4754</td>
      <td>Wed Dec 18 15:48:45 +0000 2013</td>
      <td>6610</td>
      <td>6610</td>
      <td>We have begun manufacturing the Mac Pro in Aus...</td>
    </tr>
    <tr>
      <th>534</th>
      <td>0.8858</td>
      <td>Wed Dec 18 04:17:26 +0000 2013</td>
      <td>1312</td>
      <td>1312</td>
      <td>Happy Holidays to all of our amazing customers...</td>
    </tr>
    <tr>
      <th>535</th>
      <td>0.7712</td>
      <td>Mon Dec 09 14:56:13 +0000 2013</td>
      <td>514</td>
      <td>514</td>
      <td>Honored that #Apple is being recognized by the...</td>
    </tr>
    <tr>
      <th>536</th>
      <td>0.3365</td>
      <td>Sun Dec 08 02:27:48 +0000 2013</td>
      <td>501</td>
      <td>501</td>
      <td>SEC champs! Shout out for all of the players a...</td>
    </tr>
    <tr>
      <th>537</th>
      <td>0.0000</td>
      <td>Fri Dec 06 12:43:36 +0000 2013</td>
      <td>1699</td>
      <td>1699</td>
      <td>“ What counts in life is not the mere fact tha...</td>
    </tr>
    <tr>
      <th>538</th>
      <td>0.9325</td>
      <td>Fri Dec 06 01:39:47 +0000 2013</td>
      <td>1722</td>
      <td>1722</td>
      <td>Amazing human being. Champion of freedom and h...</td>
    </tr>
    <tr>
      <th>539</th>
      <td>0.5106</td>
      <td>Sun Dec 01 14:08:42 +0000 2013</td>
      <td>4138</td>
      <td>4138</td>
      <td>We are marking #World AIDS Day by turning Appl...</td>
    </tr>
    <tr>
      <th>540</th>
      <td>-0.5195</td>
      <td>Sun Dec 01 00:57:27 +0000 2013</td>
      <td>1298</td>
      <td>1298</td>
      <td>I'll never tire of listening to this!  Could n...</td>
    </tr>
    <tr>
      <th>541</th>
      <td>0.9474</td>
      <td>Sun Dec 01 00:29:34 +0000 2013</td>
      <td>6551</td>
      <td>6551</td>
      <td>RT @espn: AUBURN WINS!! AUBURN WINS!!! AUBURN ...</td>
    </tr>
    <tr>
      <th>542</th>
      <td>0.9508</td>
      <td>Thu Nov 28 14:38:53 +0000 2013</td>
      <td>1007</td>
      <td>1007</td>
      <td>Grateful this #Thanksgiving for amazing custom...</td>
    </tr>
    <tr>
      <th>543</th>
      <td>-0.0790</td>
      <td>Sat Nov 23 21:04:16 +0000 2013</td>
      <td>187</td>
      <td>187</td>
      <td>Very proud of the Blue Devils.  https://t.co/3...</td>
    </tr>
    <tr>
      <th>544</th>
      <td>0.6808</td>
      <td>Fri Nov 22 19:50:14 +0000 2013</td>
      <td>220</td>
      <td>220</td>
      <td>RT @KerryKennedyRFK: “If we cannot end now our...</td>
    </tr>
    <tr>
      <th>545</th>
      <td>-0.6597</td>
      <td>Fri Nov 22 19:15:02 +0000 2013</td>
      <td>1322</td>
      <td>1322</td>
      <td>Timeless advice.  "Let both sides explore what...</td>
    </tr>
    <tr>
      <th>546</th>
      <td>-0.3400</td>
      <td>Sun Nov 17 00:52:11 +0000 2013</td>
      <td>87</td>
      <td>87</td>
      <td>RT @TheAUPlainsman: FINAL: No. 7 Auburn 43, No...</td>
    </tr>
    <tr>
      <th>547</th>
      <td>0.8313</td>
      <td>Thu Nov 07 20:43:34 +0000 2013</td>
      <td>718</td>
      <td>718</td>
      <td>Thanks to all Senators who supported ENDA!  I ...</td>
    </tr>
    <tr>
      <th>548</th>
      <td>0.0000</td>
      <td>Mon Nov 04 19:46:03 +0000 2013</td>
      <td>388</td>
      <td>388</td>
      <td>http://t.co/PjGkNqNREn</td>
    </tr>
    <tr>
      <th>549</th>
      <td>0.5106</td>
      <td>Tue Oct 22 16:20:39 +0000 2013</td>
      <td>4778</td>
      <td>4778</td>
      <td>Can't wait to get underway. Having fun backstage.</td>
    </tr>
    <tr>
      <th>550</th>
      <td>0.6588</td>
      <td>Fri Oct 18 17:01:57 +0000 2013</td>
      <td>235</td>
      <td>235</td>
      <td>Looking forward to a great season!  https://t....</td>
    </tr>
    <tr>
      <th>551</th>
      <td>0.8074</td>
      <td>Wed Oct 16 13:08:08 +0000 2013</td>
      <td>2516</td>
      <td>2516</td>
      <td>Our home for innovation and creativity for dec...</td>
    </tr>
    <tr>
      <th>552</th>
      <td>0.5081</td>
      <td>Sun Oct 13 21:21:59 +0000 2013</td>
      <td>324</td>
      <td>324</td>
      <td>Very proud of the Tigers! “@TheAUPlainsman: Au...</td>
    </tr>
    <tr>
      <th>553</th>
      <td>-0.2500</td>
      <td>Sat Oct 05 14:10:45 +0000 2013</td>
      <td>9332</td>
      <td>9332</td>
      <td>Second anniversary of Steve's death. Going on ...</td>
    </tr>
    <tr>
      <th>554</th>
      <td>0.8908</td>
      <td>Mon Sep 23 15:59:29 +0000 2013</td>
      <td>2639</td>
      <td>2639</td>
      <td>Thanks to all our amazing customers for the fa...</td>
    </tr>
    <tr>
      <th>555</th>
      <td>0.4201</td>
      <td>Sun Sep 22 12:05:30 +0000 2013</td>
      <td>3068</td>
      <td>3068</td>
      <td>RT @ConanOBrien: iOS7? More like iOSHeaven. #A...</td>
    </tr>
    <tr>
      <th>556</th>
      <td>0.6096</td>
      <td>Fri Sep 20 19:02:22 +0000 2013</td>
      <td>7019</td>
      <td>7019</td>
      <td>Visited Retail Stores in Palo Alto today. Seei...</td>
    </tr>
  </tbody>
</table>
<p>557 rows × 5 columns</p>
</div>




```python
for date in tweets['Date']:
   dt=datetime.datetime.strptime(date, "%a %b %d %H:%M:%S %z %Y")
```


```python
apple_tweets=tweets[tweets['Text'].str.contains('Apple')]
apple_tweets
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Compound</th>
      <th>Date</th>
      <th>Favorite Count</th>
      <th>Retweet Count</th>
      <th>Text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0.0000</td>
      <td>Mon Apr 09 22:57:32 +0000 2018</td>
      <td>17233</td>
      <td>17233</td>
      <td>Every Apple store, every data center, every Ap...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.3818</td>
      <td>Mon Apr 09 13:30:21 +0000 2018</td>
      <td>2266</td>
      <td>2266</td>
      <td>Thanks to Apple customers around the world for...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.6114</td>
      <td>Sat Apr 07 04:42:04 +0000 2018</td>
      <td>1125</td>
      <td>1125</td>
      <td>Apple loves Tokyo and our customers, employees...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.3862</td>
      <td>Tue Apr 03 21:52:26 +0000 2018</td>
      <td>7349</td>
      <td>7349</td>
      <td>From everyone at Apple, we send our sympathy a...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>0.0000</td>
      <td>Mon Apr 09 22:57:32 +0000 2018</td>
      <td>17233</td>
      <td>17233</td>
      <td>Every Apple store, every data center, every Ap...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>0.3818</td>
      <td>Mon Apr 09 13:30:21 +0000 2018</td>
      <td>2266</td>
      <td>2266</td>
      <td>Thanks to Apple customers around the world for...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>0.6114</td>
      <td>Sat Apr 07 04:42:04 +0000 2018</td>
      <td>1125</td>
      <td>1125</td>
      <td>Apple loves Tokyo and our customers, employees...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>0.3862</td>
      <td>Tue Apr 03 21:52:26 +0000 2018</td>
      <td>7349</td>
      <td>7349</td>
      <td>From everyone at Apple, we send our sympathy a...</td>
    </tr>
    <tr>
      <th>43</th>
      <td>0.4939</td>
      <td>Sat Feb 24 16:53:46 +0000 2018</td>
      <td>15452</td>
      <td>15452</td>
      <td>Remembering Steve, our friend and leader, on h...</td>
    </tr>
    <tr>
      <th>48</th>
      <td>0.6580</td>
      <td>Fri Feb 09 21:08:22 +0000 2018</td>
      <td>1028</td>
      <td>1028</td>
      <td>Hey Siri, play my weekend playlist! Excited to...</td>
    </tr>
    <tr>
      <th>49</th>
      <td>0.7901</td>
      <td>Thu Feb 08 14:34:25 +0000 2018</td>
      <td>1209</td>
      <td>1209</td>
      <td>Time to do something good for your heart! Earn...</td>
    </tr>
    <tr>
      <th>50</th>
      <td>0.8622</td>
      <td>Tue Feb 06 20:42:48 +0000 2018</td>
      <td>822</td>
      <td>822</td>
      <td>Listen up! @TechCrunch says: "Apple’s HomePod ...</td>
    </tr>
    <tr>
      <th>59</th>
      <td>0.9423</td>
      <td>Mon Jan 22 13:59:51 +0000 2018</td>
      <td>2884</td>
      <td>2884</td>
      <td>Apple is proud to support the courageous, visi...</td>
    </tr>
    <tr>
      <th>60</th>
      <td>0.5574</td>
      <td>Fri Jan 19 17:11:29 +0000 2018</td>
      <td>521</td>
      <td>521</td>
      <td>Thanks to the students, teachers and staff @Ha...</td>
    </tr>
    <tr>
      <th>61</th>
      <td>0.6688</td>
      <td>Thu Jan 18 02:20:38 +0000 2018</td>
      <td>420</td>
      <td>420</td>
      <td>Hello from the biggest little store in the App...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>0.6114</td>
      <td>Tue Jan 16 23:30:04 +0000 2018</td>
      <td>209</td>
      <td>209</td>
      <td>It was a pleasure talking to you, @rebeccaekah...</td>
    </tr>
    <tr>
      <th>64</th>
      <td>0.6369</td>
      <td>Mon Jan 15 22:07:35 +0000 2018</td>
      <td>794</td>
      <td>794</td>
      <td>MLK reminded us to live our values and serve o...</td>
    </tr>
    <tr>
      <th>70</th>
      <td>0.7783</td>
      <td>Fri Dec 22 20:51:53 +0000 2017</td>
      <td>1069</td>
      <td>1069</td>
      <td>Here’s to the tens of thousands of dedicated A...</td>
    </tr>
    <tr>
      <th>71</th>
      <td>0.0000</td>
      <td>Thu Dec 21 15:09:08 +0000 2017</td>
      <td>2997</td>
      <td>2997</td>
      <td>You never know who you’ll run into on the Appl...</td>
    </tr>
    <tr>
      <th>79</th>
      <td>0.6808</td>
      <td>Sat Dec 09 20:37:07 +0000 2017</td>
      <td>574</td>
      <td>574</td>
      <td>Thanks to the Apple team for our biggest @Toys...</td>
    </tr>
    <tr>
      <th>81</th>
      <td>0.8126</td>
      <td>Fri Dec 08 02:53:03 +0000 2017</td>
      <td>977</td>
      <td>977</td>
      <td>Imagination and creativity drives us at Apple....</td>
    </tr>
    <tr>
      <th>82</th>
      <td>0.6369</td>
      <td>Wed Dec 06 23:23:30 +0000 2017</td>
      <td>962</td>
      <td>962</td>
      <td>Thank you @JustinTrudeau on behalf of our Cana...</td>
    </tr>
    <tr>
      <th>89</th>
      <td>0.9285</td>
      <td>Thu Nov 23 16:47:53 +0000 2017</td>
      <td>1463</td>
      <td>1463</td>
      <td>Happy #Thanksgiving! Grateful this year for fa...</td>
    </tr>
    <tr>
      <th>98</th>
      <td>0.0000</td>
      <td>Wed Nov 01 19:23:20 +0000 2017</td>
      <td>2117</td>
      <td>2117</td>
      <td>Gotta wait til Friday! Meet me at the Apple St...</td>
    </tr>
    <tr>
      <th>101</th>
      <td>0.8834</td>
      <td>Sat Oct 21 21:28:47 +0000 2017</td>
      <td>299</td>
      <td>299</td>
      <td>Thanks @ChicagosMayor for a great conversation...</td>
    </tr>
    <tr>
      <th>108</th>
      <td>0.9230</td>
      <td>Wed Oct 11 13:36:57 +0000 2017</td>
      <td>589</td>
      <td>589</td>
      <td>Robot dance party! 🤖 Thanks to these talented ...</td>
    </tr>
    <tr>
      <th>109</th>
      <td>0.8777</td>
      <td>Tue Oct 10 15:45:58 +0000 2017</td>
      <td>1127</td>
      <td>1127</td>
      <td>Our thoughts are with our Bay Area friends &amp;am...</td>
    </tr>
    <tr>
      <th>114</th>
      <td>0.2960</td>
      <td>Fri Oct 06 21:50:21 +0000 2017</td>
      <td>736</td>
      <td>736</td>
      <td>Saluting the many #womenintech representing Ap...</td>
    </tr>
    <tr>
      <th>116</th>
      <td>0.8074</td>
      <td>Tue Oct 03 18:48:10 +0000 2017</td>
      <td>607</td>
      <td>607</td>
      <td>Our condolences to the Otellini family and eve...</td>
    </tr>
    <tr>
      <th>121</th>
      <td>0.3818</td>
      <td>Thu Sep 28 23:20:48 +0000 2017</td>
      <td>2406</td>
      <td>2406</td>
      <td>At Apple, we believe privacy is a fundamental ...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>444</th>
      <td>0.5106</td>
      <td>Mon Dec 08 15:10:09 +0000 2014</td>
      <td>512</td>
      <td>512</td>
      <td>Join us for the #HourofCode. Create something....</td>
    </tr>
    <tr>
      <th>445</th>
      <td>0.4767</td>
      <td>Tue Dec 02 00:06:14 +0000 2014</td>
      <td>335</td>
      <td>335</td>
      <td>RT @debdugan: Proud to spend #WorldAIDSDay wit...</td>
    </tr>
    <tr>
      <th>446</th>
      <td>0.6249</td>
      <td>Mon Dec 01 23:31:15 +0000 2014</td>
      <td>818</td>
      <td>818</td>
      <td>Apple stores around the world are RED today fo...</td>
    </tr>
    <tr>
      <th>447</th>
      <td>0.4588</td>
      <td>Thu Nov 27 16:24:53 +0000 2014</td>
      <td>1012</td>
      <td>1012</td>
      <td>Grateful to be a small part of the Apple commu...</td>
    </tr>
    <tr>
      <th>449</th>
      <td>0.8481</td>
      <td>Wed Nov 19 15:10:33 +0000 2014</td>
      <td>743</td>
      <td>743</td>
      <td>Celebrating another 100% score on the HRC's Co...</td>
    </tr>
    <tr>
      <th>450</th>
      <td>0.5994</td>
      <td>Mon Nov 17 01:12:16 +0000 2014</td>
      <td>1577</td>
      <td>1577</td>
      <td>Using Apple Pay at Whole Foods. Easy, Private,...</td>
    </tr>
    <tr>
      <th>458</th>
      <td>0.7783</td>
      <td>Thu Oct 16 14:18:54 +0000 2014</td>
      <td>2567</td>
      <td>2567</td>
      <td>Looking forward to this morning's event. Hope ...</td>
    </tr>
    <tr>
      <th>461</th>
      <td>0.7351</td>
      <td>Tue Sep 30 13:38:48 +0000 2014</td>
      <td>12954</td>
      <td>12954</td>
      <td>Amazing to see the excited crowds today in Par...</td>
    </tr>
    <tr>
      <th>462</th>
      <td>0.4767</td>
      <td>Mon Sep 22 22:00:46 +0000 2014</td>
      <td>713</td>
      <td>713</td>
      <td>Proud to represent Apple at #CWNYC. The time f...</td>
    </tr>
    <tr>
      <th>463</th>
      <td>0.6996</td>
      <td>Sat Sep 20 23:38:48 +0000 2014</td>
      <td>984</td>
      <td>984</td>
      <td>A shout-out to 3000 Apple employees and their ...</td>
    </tr>
    <tr>
      <th>465</th>
      <td>0.3612</td>
      <td>Tue Sep 09 18:08:02 +0000 2014</td>
      <td>6493</td>
      <td>6493</td>
      <td>One More Thing. Having the time of my life. It...</td>
    </tr>
    <tr>
      <th>467</th>
      <td>0.7644</td>
      <td>Tue Sep 09 12:56:29 +0000 2014</td>
      <td>14409</td>
      <td>14409</td>
      <td>Looking forward to a great day in Cupertino! J...</td>
    </tr>
    <tr>
      <th>468</th>
      <td>0.8687</td>
      <td>Thu Sep 04 22:48:01 +0000 2014</td>
      <td>5857</td>
      <td>5857</td>
      <td>Apple - Live - Countdown to the Apple Special ...</td>
    </tr>
    <tr>
      <th>471</th>
      <td>0.0772</td>
      <td>Fri Aug 15 11:15:03 +0000 2014</td>
      <td>3336</td>
      <td>3336</td>
      <td>Took the ALS #IceBucketChallenge with @michael...</td>
    </tr>
    <tr>
      <th>475</th>
      <td>0.5106</td>
      <td>Wed Aug 06 15:19:26 +0000 2014</td>
      <td>776</td>
      <td>776</td>
      <td>Apple &amp;amp; the App Store are having a huge im...</td>
    </tr>
    <tr>
      <th>476</th>
      <td>0.7901</td>
      <td>Tue Aug 05 17:22:11 +0000 2014</td>
      <td>716</td>
      <td>716</td>
      <td>Thanks to our amazing developer community!  Ap...</td>
    </tr>
    <tr>
      <th>480</th>
      <td>0.5411</td>
      <td>Wed Jul 16 01:45:10 +0000 2014</td>
      <td>3417</td>
      <td>3417</td>
      <td>Today Apple and IBM announced a landmark enter...</td>
    </tr>
    <tr>
      <th>483</th>
      <td>0.8271</td>
      <td>Sun Jun 29 22:02:55 +0000 2014</td>
      <td>3861</td>
      <td>3861</td>
      <td>Congrats to 5000 Apple employees/families who ...</td>
    </tr>
    <tr>
      <th>485</th>
      <td>0.8398</td>
      <td>Mon Jun 23 05:04:59 +0000 2014</td>
      <td>1792</td>
      <td>1792</td>
      <td>Congratulations to this amazing team at the ne...</td>
    </tr>
    <tr>
      <th>491</th>
      <td>0.8908</td>
      <td>Thu Jun 12 04:01:09 +0000 2014</td>
      <td>1706</td>
      <td>1706</td>
      <td>A stunning new Apple Store opens Friday in Tok...</td>
    </tr>
    <tr>
      <th>493</th>
      <td>0.7964</td>
      <td>Fri Jun 06 16:26:29 +0000 2014</td>
      <td>1430</td>
      <td>1430</td>
      <td>Our AppleCare team is the best in the world. T...</td>
    </tr>
    <tr>
      <th>496</th>
      <td>0.8957</td>
      <td>Wed May 28 22:32:30 +0000 2014</td>
      <td>5730</td>
      <td>5730</td>
      <td>Sharing a laugh with Jimmy, Dre, and @cue. Exc...</td>
    </tr>
    <tr>
      <th>498</th>
      <td>0.7378</td>
      <td>Sat May 10 16:22:49 +0000 2014</td>
      <td>433</td>
      <td>433</td>
      <td>Join me for lunch and advance human rights @rf...</td>
    </tr>
    <tr>
      <th>500</th>
      <td>0.8316</td>
      <td>Tue Apr 22 23:31:20 +0000 2014</td>
      <td>697</td>
      <td>697</td>
      <td>Celebrating Earth Day with Jack Johnson at App...</td>
    </tr>
    <tr>
      <th>507</th>
      <td>0.6696</td>
      <td>Fri Apr 04 18:08:26 +0000 2014</td>
      <td>558</td>
      <td>558</td>
      <td>RT @RED: Great news to end the week! Apple's t...</td>
    </tr>
    <tr>
      <th>517</th>
      <td>0.7346</td>
      <td>Fri Feb 14 05:13:09 +0000 2014</td>
      <td>653</td>
      <td>653</td>
      <td>I'm tremendously proud of the progress Apple m...</td>
    </tr>
    <tr>
      <th>535</th>
      <td>0.7712</td>
      <td>Mon Dec 09 14:56:13 +0000 2013</td>
      <td>514</td>
      <td>514</td>
      <td>Honored that #Apple is being recognized by the...</td>
    </tr>
    <tr>
      <th>539</th>
      <td>0.5106</td>
      <td>Sun Dec 01 14:08:42 +0000 2013</td>
      <td>4138</td>
      <td>4138</td>
      <td>We are marking #World AIDS Day by turning Appl...</td>
    </tr>
    <tr>
      <th>551</th>
      <td>0.8074</td>
      <td>Wed Oct 16 13:08:08 +0000 2013</td>
      <td>2516</td>
      <td>2516</td>
      <td>Our home for innovation and creativity for dec...</td>
    </tr>
    <tr>
      <th>555</th>
      <td>0.4201</td>
      <td>Sun Sep 22 12:05:30 +0000 2013</td>
      <td>3068</td>
      <td>3068</td>
      <td>RT @ConanOBrien: iOS7? More like iOSHeaven. #A...</td>
    </tr>
  </tbody>
</table>
<p>130 rows × 5 columns</p>
</div>




```python
daily_dt=pd.to_datetime(apple_tweets['Date']).dt.to_period('d')
monthly_dt=pd.to_datetime(apple_tweets['Date']).dt.to_period('m')
yearly_dt=pd.to_datetime(apple_tweets['Date']).dt.to_period('y')
```


```python
apple_tweets["Daily Date"]=daily_dt
apple_tweets["Monthly Date"]=monthly_dt
apple_tweets["Yearly Date"]=yearly_dt
```

    C:\Users\Tobin\Anaconda3\envs\PythonData\lib\site-packages\ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """Entry point for launching an IPython kernel.
    C:\Users\Tobin\Anaconda3\envs\PythonData\lib\site-packages\ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    C:\Users\Tobin\Anaconda3\envs\PythonData\lib\site-packages\ipykernel_launcher.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      This is separate from the ipykernel package so we can avoid doing imports until
    


```python
sort=apple_tweets.sort_values('Compound', ascending= True)
sort.head(100
         )
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Compound</th>
      <th>Date</th>
      <th>Favorite Count</th>
      <th>Retweet Count</th>
      <th>Text</th>
      <th>Daily Date</th>
      <th>Monthly Date</th>
      <th>Yearly Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>182</th>
      <td>-0.5574</td>
      <td>Fri Jun 02 00:36:46 +0000 2017</td>
      <td>15340</td>
      <td>15340</td>
      <td>Decision to withdraw from the #ParisAgreeement...</td>
      <td>2017-06-02</td>
      <td>2017-06</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>419</th>
      <td>-0.5256</td>
      <td>Fri Mar 27 17:56:44 +0000 2015</td>
      <td>13661</td>
      <td>13661</td>
      <td>Apple is open for everyone. We are deeply disa...</td>
      <td>2015-03-27</td>
      <td>2015-03</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>130</th>
      <td>-0.3818</td>
      <td>Tue Sep 05 18:33:23 +0000 2017</td>
      <td>13046</td>
      <td>13046</td>
      <td>#Dreamers contribute to our companies and our ...</td>
      <td>2017-09-05</td>
      <td>2017-09</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>264</th>
      <td>-0.1027</td>
      <td>Thu Oct 13 10:15:18 +0000 2016</td>
      <td>2536</td>
      <td>2536</td>
      <td>Just rode JRE's Yamanote line with Apple Pay. ...</td>
      <td>2016-10-13</td>
      <td>2016-10</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0000</td>
      <td>Mon Apr 09 22:57:32 +0000 2018</td>
      <td>17233</td>
      <td>17233</td>
      <td>Every Apple store, every data center, every Ap...</td>
      <td>2018-04-09</td>
      <td>2018-04</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>142</th>
      <td>0.0000</td>
      <td>Thu Aug 24 19:46:43 +0000 2017</td>
      <td>386</td>
      <td>386</td>
      <td>Looking forward to working with @KimReynoldsIA...</td>
      <td>2017-08-24</td>
      <td>2017-08</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>160</th>
      <td>0.0000</td>
      <td>Thu Jun 29 16:41:04 +0000 2017</td>
      <td>16791</td>
      <td>16791</td>
      <td>Here's to the #iPhone that changed the world, ...</td>
      <td>2017-06-29</td>
      <td>2017-06</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>171</th>
      <td>0.0000</td>
      <td>Sun Jun 11 20:54:44 +0000 2017</td>
      <td>2670</td>
      <td>2670</td>
      <td>Here comes Apple Taipei 101, our first store i...</td>
      <td>2017-06-11</td>
      <td>2017-06</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>98</th>
      <td>0.0000</td>
      <td>Wed Nov 01 19:23:20 +0000 2017</td>
      <td>2117</td>
      <td>2117</td>
      <td>Gotta wait til Friday! Meet me at the Apple St...</td>
      <td>2017-11-01</td>
      <td>2017-11</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>209</th>
      <td>0.0000</td>
      <td>Sat Mar 25 16:34:12 +0000 2017</td>
      <td>700</td>
      <td>700</td>
      <td>RT @RED: "Keeping inc(red)ible company... Appl...</td>
      <td>2017-03-25</td>
      <td>2017-03</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>219</th>
      <td>0.0000</td>
      <td>Wed Feb 22 14:34:12 +0000 2017</td>
      <td>5110</td>
      <td>5110</td>
      <td>The campus Steve envisioned will be known as A...</td>
      <td>2017-02-22</td>
      <td>2017-02</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>256</th>
      <td>0.0000</td>
      <td>Fri Oct 28 17:05:29 +0000 2016</td>
      <td>768</td>
      <td>768</td>
      <td>👏 to customers around the world who are pickin...</td>
      <td>2016-10-28</td>
      <td>2016-10</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>71</th>
      <td>0.0000</td>
      <td>Thu Dec 21 15:09:08 +0000 2017</td>
      <td>2997</td>
      <td>2997</td>
      <td>You never know who you’ll run into on the Appl...</td>
      <td>2017-12-21</td>
      <td>2017-12</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>268</th>
      <td>0.0000</td>
      <td>Sat Oct 08 00:41:27 +0000 2016</td>
      <td>1515</td>
      <td>1515</td>
      <td>Shukriya India and everyone who turned out for...</td>
      <td>2016-10-08</td>
      <td>2016-10</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>278</th>
      <td>0.0000</td>
      <td>Fri Sep 16 11:27:06 +0000 2016</td>
      <td>1939</td>
      <td>1939</td>
      <td>It’s time! #iPhone7 and #AppleWatchSeries2 are...</td>
      <td>2016-09-16</td>
      <td>2016-09</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>351</th>
      <td>0.0000</td>
      <td>Wed Dec 09 20:54:36 +0000 2015</td>
      <td>587</td>
      <td>587</td>
      <td>Just met coders of tomorrow from NY's PS 57. #...</td>
      <td>2015-12-09</td>
      <td>2015-12</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>413</th>
      <td>0.0000</td>
      <td>Sat Apr 18 23:45:56 +0000 2015</td>
      <td>1333</td>
      <td>1333</td>
      <td>Olá São Paulo and parabéns to our team at the ...</td>
      <td>2015-04-18</td>
      <td>2015-04</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>431</th>
      <td>0.0000</td>
      <td>Sat Jan 24 04:24:50 +0000 2015</td>
      <td>782</td>
      <td>782</td>
      <td>Starting Something New in Hangzhou, China! #Ap...</td>
      <td>2015-01-24</td>
      <td>2015-01</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>21</th>
      <td>0.0000</td>
      <td>Mon Apr 09 22:57:32 +0000 2018</td>
      <td>17233</td>
      <td>17233</td>
      <td>Every Apple store, every data center, every Ap...</td>
      <td>2018-04-09</td>
      <td>2018-04</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>123</th>
      <td>0.0000</td>
      <td>Fri Sep 22 21:47:36 +0000 2017</td>
      <td>810</td>
      <td>810</td>
      <td>The first thing you do with your new #AppleWat...</td>
      <td>2017-09-22</td>
      <td>2017-09</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>471</th>
      <td>0.0772</td>
      <td>Fri Aug 15 11:15:03 +0000 2014</td>
      <td>3336</td>
      <td>3336</td>
      <td>Took the ALS #IceBucketChallenge with @michael...</td>
      <td>2014-08-15</td>
      <td>2014-08</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>339</th>
      <td>0.2500</td>
      <td>Thu Jan 21 12:17:11 +0000 2016</td>
      <td>1947</td>
      <td>1947</td>
      <td>Apple has created over 1.4m jobs across Europe...</td>
      <td>2016-01-21</td>
      <td>2016-01</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>386</th>
      <td>0.2732</td>
      <td>Fri Aug 14 01:09:22 +0000 2015</td>
      <td>1042</td>
      <td>1042</td>
      <td>Apple is committed to making our company and t...</td>
      <td>2015-08-14</td>
      <td>2015-08</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>114</th>
      <td>0.2960</td>
      <td>Fri Oct 06 21:50:21 +0000 2017</td>
      <td>736</td>
      <td>736</td>
      <td>Saluting the many #womenintech representing Ap...</td>
      <td>2017-10-06</td>
      <td>2017-10</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>357</th>
      <td>0.3612</td>
      <td>Thu Nov 12 20:00:42 +0000 2015</td>
      <td>785</td>
      <td>785</td>
      <td>Thank you Robert for being one of our very fir...</td>
      <td>2015-11-12</td>
      <td>2015-11</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>465</th>
      <td>0.3612</td>
      <td>Tue Sep 09 18:08:02 +0000 2014</td>
      <td>6493</td>
      <td>6493</td>
      <td>One More Thing. Having the time of my life. It...</td>
      <td>2014-09-09</td>
      <td>2014-09</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>121</th>
      <td>0.3818</td>
      <td>Thu Sep 28 23:20:48 +0000 2017</td>
      <td>2406</td>
      <td>2406</td>
      <td>At Apple, we believe privacy is a fundamental ...</td>
      <td>2017-09-28</td>
      <td>2017-09</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>22</th>
      <td>0.3818</td>
      <td>Mon Apr 09 13:30:21 +0000 2018</td>
      <td>2266</td>
      <td>2266</td>
      <td>Thanks to Apple customers around the world for...</td>
      <td>2018-04-09</td>
      <td>2018-04</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.3818</td>
      <td>Mon Apr 09 13:30:21 +0000 2018</td>
      <td>2266</td>
      <td>2266</td>
      <td>Thanks to Apple customers around the world for...</td>
      <td>2018-04-09</td>
      <td>2018-04</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>28</th>
      <td>0.3862</td>
      <td>Tue Apr 03 21:52:26 +0000 2018</td>
      <td>7349</td>
      <td>7349</td>
      <td>From everyone at Apple, we send our sympathy a...</td>
      <td>2018-04-03</td>
      <td>2018-04</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>349</th>
      <td>0.7041</td>
      <td>Sat Dec 12 23:27:50 +0000 2015</td>
      <td>1347</td>
      <td>1347</td>
      <td>An important moment in the fight against clima...</td>
      <td>2015-12-12</td>
      <td>2015-12</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>427</th>
      <td>0.7263</td>
      <td>Mon Feb 23 14:36:59 +0000 2015</td>
      <td>1206</td>
      <td>1206</td>
      <td>Here’s the last of 2400 giant panels for Apple...</td>
      <td>2015-02-23</td>
      <td>2015-02</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>153</th>
      <td>0.7345</td>
      <td>Sat Jul 15 21:12:36 +0000 2017</td>
      <td>770</td>
      <td>770</td>
      <td>Join me in celebrating National Parks today! C...</td>
      <td>2017-07-15</td>
      <td>2017-07</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>517</th>
      <td>0.7346</td>
      <td>Fri Feb 14 05:13:09 +0000 2014</td>
      <td>653</td>
      <td>653</td>
      <td>I'm tremendously proud of the progress Apple m...</td>
      <td>2014-02-14</td>
      <td>2014-02</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>143</th>
      <td>0.7351</td>
      <td>Thu Aug 24 14:42:38 +0000 2017</td>
      <td>701</td>
      <td>701</td>
      <td>Thanks to the team at CTS in Cincinnati, manuf...</td>
      <td>2017-08-24</td>
      <td>2017-08</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>461</th>
      <td>0.7351</td>
      <td>Tue Sep 30 13:38:48 +0000 2014</td>
      <td>12954</td>
      <td>12954</td>
      <td>Amazing to see the excited crowds today in Par...</td>
      <td>2014-09-30</td>
      <td>2014-09</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>498</th>
      <td>0.7378</td>
      <td>Sat May 10 16:22:49 +0000 2014</td>
      <td>433</td>
      <td>433</td>
      <td>Join me for lunch and advance human rights @rf...</td>
      <td>2014-05-10</td>
      <td>2014-05</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>408</th>
      <td>0.7500</td>
      <td>Fri Apr 24 22:04:13 +0000 2015</td>
      <td>727</td>
      <td>727</td>
      <td>Hope you enjoy your new Apple Watch! https://t...</td>
      <td>2015-04-24</td>
      <td>2015-04</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>340</th>
      <td>0.7506</td>
      <td>Mon Jan 18 21:23:38 +0000 2016</td>
      <td>548</td>
      <td>548</td>
      <td>Proud to volunteer beside hundreds of Apple em...</td>
      <td>2016-01-18</td>
      <td>2016-01</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>467</th>
      <td>0.7644</td>
      <td>Tue Sep 09 12:56:29 +0000 2014</td>
      <td>14409</td>
      <td>14409</td>
      <td>Looking forward to a great day in Cupertino! J...</td>
      <td>2014-09-09</td>
      <td>2014-09</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>535</th>
      <td>0.7712</td>
      <td>Mon Dec 09 14:56:13 +0000 2013</td>
      <td>514</td>
      <td>514</td>
      <td>Honored that #Apple is being recognized by the...</td>
      <td>2013-12-09</td>
      <td>2013-12</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>439</th>
      <td>0.7717</td>
      <td>Sat Jan 03 22:51:40 +0000 2015</td>
      <td>911</td>
      <td>911</td>
      <td>Running errands this afternoon and using #Appl...</td>
      <td>2015-01-03</td>
      <td>2015-01</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>312</th>
      <td>0.7777</td>
      <td>Sat May 21 14:49:54 +0000 2016</td>
      <td>1169</td>
      <td>1169</td>
      <td>A quick visit with customers and our fantastic...</td>
      <td>2016-05-21</td>
      <td>2016-05</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>187</th>
      <td>0.7783</td>
      <td>Sat May 27 14:46:41 +0000 2017</td>
      <td>895</td>
      <td>895</td>
      <td>Congratulations team, and thanks to the thousa...</td>
      <td>2017-05-27</td>
      <td>2017-05</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>458</th>
      <td>0.7783</td>
      <td>Thu Oct 16 14:18:54 +0000 2014</td>
      <td>2567</td>
      <td>2567</td>
      <td>Looking forward to this morning's event. Hope ...</td>
      <td>2014-10-16</td>
      <td>2014-10</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>70</th>
      <td>0.7783</td>
      <td>Fri Dec 22 20:51:53 +0000 2017</td>
      <td>1069</td>
      <td>1069</td>
      <td>Here’s to the tens of thousands of dedicated A...</td>
      <td>2017-12-22</td>
      <td>2017-12</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>476</th>
      <td>0.7901</td>
      <td>Tue Aug 05 17:22:11 +0000 2014</td>
      <td>716</td>
      <td>716</td>
      <td>Thanks to our amazing developer community!  Ap...</td>
      <td>2014-08-05</td>
      <td>2014-08</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>127</th>
      <td>0.7901</td>
      <td>Tue Sep 12 15:11:43 +0000 2017</td>
      <td>16969</td>
      <td>16969</td>
      <td>It's a big day at Apple! We are honored and th...</td>
      <td>2017-09-12</td>
      <td>2017-09</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>49</th>
      <td>0.7901</td>
      <td>Thu Feb 08 14:34:25 +0000 2018</td>
      <td>1209</td>
      <td>1209</td>
      <td>Time to do something good for your heart! Earn...</td>
      <td>2018-02-08</td>
      <td>2018-02</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>226</th>
      <td>0.7955</td>
      <td>Thu Feb 09 15:42:30 +0000 2017</td>
      <td>586</td>
      <td>586</td>
      <td>Great to meet @MayorofLondon today. We are inc...</td>
      <td>2017-02-09</td>
      <td>2017-02</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>228</th>
      <td>0.7959</td>
      <td>Wed Feb 08 20:34:35 +0000 2017</td>
      <td>660</td>
      <td>660</td>
      <td>Thanks Apple Buchanan Street for a warm welcom...</td>
      <td>2017-02-08</td>
      <td>2017-02</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>131</th>
      <td>0.7964</td>
      <td>Sun Sep 03 12:38:13 +0000 2017</td>
      <td>55092</td>
      <td>55092</td>
      <td>250 of my Apple coworkers are #Dreamers. I sta...</td>
      <td>2017-09-03</td>
      <td>2017-09</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>493</th>
      <td>0.7964</td>
      <td>Fri Jun 06 16:26:29 +0000 2014</td>
      <td>1430</td>
      <td>1430</td>
      <td>Our AppleCare team is the best in the world. T...</td>
      <td>2014-06-06</td>
      <td>2014-06</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>196</th>
      <td>0.8016</td>
      <td>Fri Apr 28 01:30:43 +0000 2017</td>
      <td>716</td>
      <td>716</td>
      <td>Gorgeous store, phenomenal team! Thanks to eve...</td>
      <td>2017-04-28</td>
      <td>2017-04</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>194</th>
      <td>0.8070</td>
      <td>Thu May 18 02:13:08 +0000 2017</td>
      <td>420</td>
      <td>420</td>
      <td>Thanks @JamesRath @PintSzDiva @RikkiPoynter fo...</td>
      <td>2017-05-18</td>
      <td>2017-05</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>116</th>
      <td>0.8074</td>
      <td>Tue Oct 03 18:48:10 +0000 2017</td>
      <td>607</td>
      <td>607</td>
      <td>Our condolences to the Otellini family and eve...</td>
      <td>2017-10-03</td>
      <td>2017-10</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>551</th>
      <td>0.8074</td>
      <td>Wed Oct 16 13:08:08 +0000 2013</td>
      <td>2516</td>
      <td>2516</td>
      <td>Our home for innovation and creativity for dec...</td>
      <td>2013-10-16</td>
      <td>2013-10</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>415</th>
      <td>0.8122</td>
      <td>Fri Apr 10 22:00:08 +0000 2015</td>
      <td>1405</td>
      <td>1405</td>
      <td>Thrilled to see so many customers—all around t...</td>
      <td>2015-04-10</td>
      <td>2015-04</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>139</th>
      <td>0.8122</td>
      <td>Thu Aug 24 21:03:01 +0000 2017</td>
      <td>406</td>
      <td>406</td>
      <td>Great day in the Hawkeye State! A shout out to...</td>
      <td>2017-08-24</td>
      <td>2017-08</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>81</th>
      <td>0.8126</td>
      <td>Fri Dec 08 02:53:03 +0000 2017</td>
      <td>977</td>
      <td>977</td>
      <td>Imagination and creativity drives us at Apple....</td>
      <td>2017-12-08</td>
      <td>2017-12</td>
      <td>2017</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 8 columns</p>
</div>




```python
Daily_avg=apple_tweets.groupby('Daily Date')['Compound'].mean()
Daily_dataframe=pd.DataFrame({'Daily Comp Score':Daily_avg})
Daily_dataframe.plot(kind='line',y='Daily Comp Score' ,linestyle='None', marker='o',figsize=(10,10))
```




    <matplotlib.axes._subplots.AxesSubplot at 0x293766f7f28>




![png](output_8_1.png)



```python
Monthly_avg=apple_tweets.groupby('Monthly Date')['Compound'].mean()
Monthly_dataframe=pd.DataFrame({'Monthly Comp Score':Monthly_avg})
Monthly_dataframe.plot(kind='line',y='Monthly Comp Score' ,linestyle='None', marker='o',figsize=(10,10))
```




    <matplotlib.axes._subplots.AxesSubplot at 0x29377a01208>




![png](output_9_1.png)



```python
bins = [-1.0,-0.5,0,0.5,1.0]

# Create labels for these bins
group_labels = ["Really Pessimistic","Mildy mad","having a nice day",
                "totally chilled"]
group= ['-1.0 to -0.5','-0.5 to 0.0','0.0 to 0.5','0.5 to 1.0']
```


```python
Daily_dataframe['Comp Group']= pd.cut(Daily_dataframe["Daily Comp Score"],bins,labels=group)
d=Daily_dataframe.groupby('Comp Group').count()
d
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Daily Comp Score</th>
    </tr>
    <tr>
      <th>Comp Group</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>-1.0 to -0.5</th>
      <td>2</td>
    </tr>
    <tr>
      <th>-0.5 to 0.0</th>
      <td>14</td>
    </tr>
    <tr>
      <th>0.0 to 0.5</th>
      <td>20</td>
    </tr>
    <tr>
      <th>0.5 to 1.0</th>
      <td>83</td>
    </tr>
  </tbody>
</table>
</div>




```python

#d.plot(kind='pie',y='Daily Comp Score', autopct= '%1.1f%%', figsize=(6,6),labels=['','','','',''])
compound = d

value = compound
explode= (0.05, .05, .05, 0.05)
labels= ('-1 to -.5','-.5 to 0','0 to .5','.5 to 1')
color= ["grey", "lightgrey", "darkgrey", "black", ]
plt.pie(value, explode=explode,
       autopct="%1.1f%%", shadow=True, startangle=199)
plt.axis('equal')
plt.title('Tim Cook Tweet Sentiment')
lgn=plt.legend(title='Sentiment Scores', loc="best")
plt.legend(['-1 to -.5','-.5 to 0','0 to .5','.5 to 1'])
plt.show()
```

    No handles with labels found to put in legend.
    


![png](output_12_1.png)



```python
tweets.to_csv("cook.csv", index=False, header=True)
```
