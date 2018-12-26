
# Threat landscape and ratings

Often we pen test apps that'll be internal to a client, with IP whitelisting in place to restrict access, making for less than 100 possible threat actors. Even if someone pwns the app to high heaven the worst they'll get is maybe SSNs.

Those "normal" web apps aren't holding digital cash. They aren't holding potentially millions of dollars in tokens some bad apple could run off with. And the source code to those apps isn't (more or less) showing. And not just anybody can access them. Not just anybody can call them.

That's the case here. That's what we are dealing with. This is high stakes security like you might not have seen previously.

You (or your clients) want to be damned sure of the contracts you put out.

Immutability is a big tenet of blockchain. Once you deploy a smart contract to the Ethereum mainnet, it's nearly impossible to change. Code is law. Unless you programmed in "upgradeability", which introduces a whole lot of inherent risk by itself.

We'll start this Ethereum security journey with just the contract files in scope. Either .sol files or EVM bytecode.

Are you up to the challenge?

## "High, medium, low" = out the window

Before talking issues let's talk about rating them.

When we pen test web apps the "OWASP way", we typically rate findings with a table like below.

`TODO`

This course's authors (plus smarter people than us!) are of the opinion this isn't appropriate for Ethereum contracts. Remember the immutability.

`TODO`

# What could possibly go wrong?!

Turns out a whole slew of stuff can go wrong with Ethereum contracts. And it has.

`TODO example 1`

`TODO example 2`

`TODO example 3`

But don't fear. Any of these issues can be found in code review. Any known issues.

So we'll start there with "pure" code review. No tools. Just like a good pen tester shouldn't need Burp Suite.

## Required reading

Read through the following for a comprehensive introduction to different vulnerabilities.

`TODO links`

This should be more of a skim than a full ingestion. We advise against even taking notes. This content will be driven home with later exercises/drills.

It might be useful to re-skim this stuff before bedtime for several nights too. Immerse yourself in Ethereum vulnerabilities.
