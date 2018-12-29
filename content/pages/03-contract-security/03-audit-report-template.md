Title: Audit Report Template
Date: 2018-12-29
Modified: 2018-12-29
Category: contract-security
Tags: contract-security
Slug: contract-security/audit-report-template
Authors: Randy Gingeleski
Summary: Audit Report Template
ParentNumber: 3
ParentCategory: Contract Security
PageNumber: 3
Template: course_page


# Audit report template

*Since we are on the topic, here is a template you're free to use for audit reports.*

*It's a little opinionated in some ways. You can certainly just use only part of it or none at all...*

The title should describe the contract or contract system this report pertains to followed by some standard service name (i.e. "Contract Security Audit").

Examples:

```
Favvom Contract Security Audit
Favvom Multisig Contract Security Audit
SRQj Contract Security Audit
```

It's recommended that your overall title use capitalization like a book title but then your later headings "Do capitalization like this".

Your report might then continue into the following...

## Table of contents

- Introduction
    - Disclaimer
    - Document structure
    - Overview
- Audit summary
    - Per-contract vulnerability summary
- Summary of findings
- Detailed findings
    - Example finding 1
    - Example finding 2
    - Example finding n
- Appendix A: Test suite
- Appendix B: Finding rating classification

## Introduction

Ethereum Security Blog was retained by Acme Corp to perform a security audit on their `Acmechain` contract...

### Disclaimer

Ethereum Security Blog makes every effort but is in no way responsible for...

### Document structure

The first section contains an overview of the contract functionality contained in the scope of this security audit...

### Overview

The `Acmechain` serves multiple purposes...

## Audit summary

This security audit was conducted on the version of `Acmechain` contained within the Git commit of hash [8a7b840](#). This included the file `Acmechain.sol` which instantiates one contract (`Acmechain`) and one library (`Acmemath`).

### Per-contract vulnerability summary

**Acmemath** (`Acmechain.sol`)

No findings to report.

**Acmechain** (`Acmechain.sol`)

2 must fix findings, 1 informational finding.

## Summary of findings

| ID | Name              | Classification |
|----|-------------------|----------------|
| 1  | Example finding 1 | Must fix       |
| 2  | Example finding 2 | Must fix       |
| n  | Example finding n | Informational  |

## Detailed findings

### Example finding 1

**Classification:** Must fix

**Asset:** `AcmeChain.sol`

**Description**

Lorem ipsum blah blah blah.

**Recommendations**

Lorem ipsum blah blah blah.

### Example finding 2

**Classification:** Must fix

**Asset:** `AcmeChain.sol`

**Description**

Lorem ipsum blah blah blah.

**Recommendations**

Lorem ipsum blah blah blah.

### Example finding n

**Classification:** Informational

**Asset:** `AcmeChain.sol`

**Description**

Lorem ipsum blah blah blah.

**Recommendations**

Lorem ipsum blah blah blah.

## Appendix A: Test cases

*(Ideally work out something here with test cases, hopefully automated ones, as a value-add to the customer)*

## Appendix B: Finding rating classification

Some pop-up firms doing smart contract audits have chosen to take an "OWASP-like" approach to this. See the table below.

They also tend to call this "vulnerability severity classification" instead of the more generalized "finding rating classification".

The writers of this course believe smart contracts, especially those out in public on the Ethereum blockchain, are a different animal. They don't warrant the same rating scale as traditional web apps. It's better to chunk findings into the following:

- Must fix
- Consider fixing
- Informational

*And* to say "findings" over "vulnerabilities" because then you get the berth for informational stuff. Like, hey we couldn't help but notice you could save some gas doing *fill-in-the-blank*.

Overall this appendix B might just contain the table below.

| Rating          | Description |
|-----------------|-------------|
| Must fix        | TODO        |
| Consider fixing | TODO        |
| Informational   | TODO        |
