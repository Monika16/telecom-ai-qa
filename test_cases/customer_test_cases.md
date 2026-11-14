# Customer Test Cases
## TC-001 — Create Customer with Valid Data
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
- First Name: John
- Last Name: Smith
- Email: john@test.com
- Address: 123 Main Street
- Phone: 4255551234
### Steps
1. Enter first name.
2. Enter last name.
3. Enter email.
4. Enter address.
5. Enter phone number.
6. Submit the form.
### Expected Result
Customer should be created successfully and a Customer ID should be displayed.

## TC-002 — Add multiple customers with different valid details.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
- First Name: John
- Last Name: Smith
- Email: john@test.com
- Address: 123 Main Street
- Phone: 4255551234
- First Name: Noel
- Last Name: Shaun
- Email: noel@test.com
- Address: 345 Main Street
- Phone: 6255771234
### Steps
1. Enter first name.
2. Enter last name.
3. Enter email.
4. Enter address.
5. Enter phone number.
6. Submit the form.

Follow the steps with both test data
### Expected Result
Customers should be created successfully and 2 different Customer ID should be displayed.
## TC-003 — Submit form with all fields blank.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Steps
1. Leave the fields blank.
2. Submit the form.
### Expected Result
Alert with message "please fill all fields" is displayed.

## TC-004 — Enter numbers in First Name.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
-  First Name: 1234.
### Steps
Enter First Name
### Expected Result
A Validation of "Numbers are not allowed" is displayed.

## TC-005 — Enter numbers in Last Name.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
- Last Name: 234.
### Steps
Enter Last Name
### Expected Result
A Validation of "Numbers are not allowed" is displayed.

## TC-006 — Enter special characters in First Name.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
- First Name: ////.
### Steps
Enter First Name
## Expected Result
A Validation of "Special characters are not allowed" is displayed.

## TC-007 — Enter special characters in Last Name.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
- Last Name: !!!!.
### Steps
Enter Last Name
## Expected Result
A Validation of "Special characters are not allowed" is displayed.

## TC-008 — Enter invalid email format.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
- Email: hhhh@gb.
### Steps
Enter Email
## Expected Result
A Validation of "Email-ID is not valid" is displayed.

## TC-009 — Enter invalid telephone format.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
- Mobile Number: hhhh.
### Steps
Enter Mobile Number
## Expected Result
A Validation of "Characters are not allowed" is displayed.

## TC-010 — Enter leading spaces in a required text field.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
- First Name: give spaces.
### Steps
Enter First Name
## Expected Result
A Validation of "First character can not have space" is displayed.

## TC-011 — Refresh the page after successful customer creation.
**Priority:** Medium
### Preconditions
User is on the Add Customer page.
### Test Data
- First Name: John
- Last Name: Smith
- Email: john@test.com
- Address: 123 Main Street
- Phone: 4255551234
### Steps
1. Enter first name.
2. Enter last name.
3. Enter email.
4. Enter address.
5. Enter phone number.
6. Submit the form.
7. Click refresh once the Customer ID is generated
## Expected Result
After refreshing the page, the Customer ID continues to be displayed and no additional customer account is created.

### TC-014: Refresh confirmation page after customer creation

**Test ID:** AC-014

**Preconditions:** Add Customer page is accessible.

**Test Steps:**
1. Enter valid customer details.
2. Submit the form.
3. Capture the displayed Customer ID.
4. Refresh the confirmation page.
5. Observe the displayed result.
6. Investigate whether a duplicate customer record was created.

**Expected Result:**
The original Customer ID should remain displayed, and no unintended duplicate customer should be created.

**Actual Result:**
Original Customer ID is displayed

**Execution Status:** Needs Investigation

### TC-028: Double-click Submit button

**Test ID:** AC-029

**Objective:** Verify that double-clicking the Submit button does not create duplicate customer records.

**Preconditions:**
- Add Customer page is accessible.
- All required customer details are available.

**Test Data:**
- First Name: John
- Last Name: Smith
- Email: john029@example.com
- Address: 123 Main Street
- Telephone: 9876543210

**Test Steps:**
1. Navigate to the Add Customer page.
2. Enter valid customer details in all required fields.
3. Double-click the Submit button.
4. Observe the application response.
5. Record the displayed Customer ID.
6. Verify whether one or multiple customer records were created.

**Expected Result:**
- The application should process the customer submission successfully.
- The confirmation page should display a valid Customer ID.
- No unintended duplicate submission should be observed.

**Actual Result:**
Customer record is generated with appropriate Customer-ID.

### TC-029: Navigate Back and Resubmit Customer Form

**Test ID:** AC-030

**Expected Result:**
The application should prevent unintended duplicate customer creation
when the same customer details are resubmitted.

**Manual Test Result:**
- Submitted valid customer details.
- Navigated back using the browser Back button.
- Previously entered values were retained.
- Clicked Submit immediately without modifying any fields.
- A second Customer ID was generated.

**Manual Execution Status:** Failed

**Automation Observation:**
- Navigated back using Playwright.
- All previously entered values were restored.
- HTML validation returned True for all fields.
- Immediate submission triggered the dialog:
  `please fill all fields`.
- After focusing and tabbing through the fields, submission worked.
- A second Customer ID was generated.

**Automation Execution Status:** Defect reproduction with workaround

**Difference Between Manual and Automation:**
Manual testing allows immediate resubmission after browser Back.
Playwright requires focus and Tab interactions before the second
submission succeeds.

**Investigation Note:**
The application may not synchronize its custom JavaScript validation
state with browser-restored form values. This requires further
investigation.


### TC-030: Correct Invalid Data and Resubmit

**Test ID:** AC-031

**Objective:** Verify that the user can correct invalid customer information and successfully resubmit the form.

**Preconditions:**
- Add Customer page is accessible.
- Customer form is displayed.

**Test Data:**

| Field      | Initial Value   | Corrected Value  |
|------------|-----------------|:----------------:|
| First Name | John            |       John       |
| Last Name  | Smith           |      Smith       |
| Email      | johnexample.com | john@example.com |
| Address    | 123 Main Street | 123 Main Street  |
| Telephone  | 9876543210      |    9876543210    |

**Test Steps:**
1. Navigate to the Add Customer page.
2. Enter valid values in all fields except Email.
3. Enter an invalid email address (`johnexample.com`).
4. Click Submit.
5. Observe the validation message or error behavior.
6. Correct the email address to `john@example.com`.
7. Click Submit again.
8. Verify that the customer confirmation page is displayed.
9. Verify that a Customer ID is generated.

**Expected Result:**
- The application should reject the invalid email address.
- The user should be able to correct the email without losing the other entered details.
- After correcting the email, the form should submit successfully.
- A Customer ID should be generated.

**Actual Result:**
- The application rejected the invalid email address (`johnexample.com`).
- The form was not submitted.
- No Customer ID was generated.
- After correcting the email to `john@example.com`, the form submitted successfully.
- A Customer ID was generated.

### TC-021: Email Containing Spaces

**Test ID:** AC-021

**Objective:** Verify that an email containing spaces is rejected.

**Test Data:**
- Email: john example@test.com

**Expected Result:**
The application should reject an email containing spaces.

**Actual Result:**
The application did not accept the email address.
An informational alert was displayed.

**Manual Execution Status:** Passed

### TC-022: Telephone Containing Letters

**Test ID:** AC-022

**Objective:** Verify that letters are not accepted in the telephone field.

**Test Data:**
- Telephone: 98765abcd1

**Expected Result:**
The application should prevent alphabetic characters.

**Actual Result:**
The application displayed a validation message:
"Characters not allowed".

**Manual Execution Status:** Passed

### TC-024: One-Character First Name

**Test ID:** AC-024

**Objective:** Verify whether a one-character first name is accepted.

**Test Data:**
- First Name: A

**Expected Result:**
The application should accept a one-character first name.

**Actual Result:**
The application accepted the first name.

**Manual Execution Status:** Passed

### TC-027: Hyphen in First Name

**Test ID:** AC-027

**Objective:** Verify whether a hyphen is allowed in the first name.

**Test Data:**
- First Name: Anne-Marie

**Expected Result:**
The application should accept a hyphenated first name.

**Actual Result:**
The application did not allow the special character.

**Manual Execution Status:** Failed


