htmltemplate_DEALCARD = """
<html>
<body>
Card Dealt: {}\n
Number of Cards left in Deck: {}
<br>
Cards in Hand: {}
<br><br>
<a href="/dealcard">Deal another Card</a>
<br><br>
<a href="/stand">See Deck</a>
</body>
</html>
""".strip()

basic_html_SEEDECK = """
<html>

<body>
The deck contains:
<br>
{}
<br><br>
<a href="/blackjack_home">New Game (play again)</a>
</body>
</html>
""".strip()

homeHTML = """
<!-- OMIS30 HTML Template-->
<p>&nbsp;</p>
<p><br />Landing/Splash Page</p>
<p>&nbsp;</p>
<p><a href="calc_home">Calculator</a></p>
<p>&nbsp;</p>
<p><a href="/blackjack_home">Blackjack</a></p>
""".strip()

blackjack_homeHTML = """
<!-- OMIS30 HTML Template-->
<p>&nbsp;</p>
<p><br />Start Game?</p>
<p>&nbsp;</p>
<p><a href="/deal">Blackjack</a></p>
""".strip()

htmltemplate_DEALCARD = """
<html>
<body>
Card Dealt: {}\n
Number of Cards left in Deck: {}
<br>
Cards in Hand: {}
<br><br>
<a href="/hit">Deal another Card (hit)</a>
<br><br>
<a href="/stand">See Deck (stand)</a>
</body>
</html>
""".strip()


calc_splashHTML = """
<!-- OMIS30 HTML Template-->

"""

calc_splashHTML = """
<!-- OMIS30 HTML Template-->
<p>&nbsp;</p>
<p>Welcome to the Calculator Landing Page. Choose a calculator below:</p>
<p>&nbsp;</p>
<ul>
<li><a href="/calc1">calc1</a></li>
<li><a href="/calc2">calc2</a></li>
</ul>""".strip()

calc1HTML = """
<!-- OMIS30 HTML Template-->
<p>&nbsp;</p>
<p>Welcome to Calculator 1 Enter your parameters below, then click submit:</p>
<p>&nbsp;</p>
<a href='/'>--go to HOME/LANDING page--</a>
<p>&nbsp;</p>
<a href='/calc_home'>--go to CALC HOME--</a>
<p>&nbsp;</p>

<p>&nbsp;</p>
<form action="/calc1result">
<p>First name:<br /> <input name="firstname" type="text" value="Mickey" /> <br /> Last name:<br /> <input name="lastname" type="text" value="Mouse" /> <br /><br /> <input type="submit" value="Submit" /></p>
<p>&nbsp;</p>
<p>These results will be sent to the endpoint '/calc1result'.</p>
</form>
""".strip()

calc1resultHTML = """
<!-- OMIS30 HTML Template-->
<p>&nbsp;</p>

<a href='/'>--go to HOME/LANDING page--</a>
<p>&nbsp;</p>
<a href='/calc_home'>--go to CALC HOME--</a>
<p>&nbsp;</p>


<p>The user entered:</p>
<p>&nbsp;</p>
<table>
<tbody>
<tr>
<td>First Name</td>
<td>{firstname_field}</td>
</tr>
<tr>
<td>Last Name</td>
<td>{lastname_field}</td>
</tr>
</tbody>
</table>
""".strip()