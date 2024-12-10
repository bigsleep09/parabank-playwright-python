class HomePageLocators:
    """
    Locators for the Home Page elements.

    Attributes:
        email_input (str): Selector for the email input field on the login form.
        password_input (str): Selector for the password input field on the login form.
        submit_button (str): Selector for the login form's submit button.
        sign_in_button (str): Selector for the sign-up button to navigate to the registration page.
    """
    email_input: str = "[id='email']"
    password_input: str = "[id='password']"
    submit_button: str = "[id='submit']"
    sign_in_button: str = "[id='signup']"


class RegistrationPageLocators:
    """
    Locators for the Registration Page elements.

    Attributes:
        first_name_input (str): Selector for the first name input field.
        last_name_input (str): Selector for the last name input field.
        email_input (str): Selector for the email input field.
        password_input (str): Selector for the password input field.
        submit_button (str): Selector for the submit button to register the user.
        cancel_button (str): Selector for the cancel button to discard changes.
    """
    first_name_input: str = "[id='firstName']"
    last_name_input: str = "[id='lastName']"
    email_input: str = "[id='email']"
    password_input: str = "[id='password']"
    submit_button: str = "[id='submit']"
    cancel_button: str = "[id='cancel']"


class ContactListPageLocators:
    """
    Locators for the Contact List Page elements.

    Attributes:
        add_new_contact_button (str): Selector for the button to add a new contact.
        contacts_table (str): Selector for the rows in the contacts table.
        logout_button (str): Selector for logout button
    """
    add_new_contact_button = "[id='add-contact']"
    contacts_table = "[id='myTable'] [class=contactTableBodyRow]"
    logout_button = "[id='logout']"


class AddContactPageLocators:
    """
    Locators for the Add Contact Page elements.

    Attributes:
        first_name_input (str): Selector for the first name input field.
        last_name_input (str): Selector for the last name input field.
        birthdate_input (str): Selector for the birthdate input field.
        email_input (str): Selector for the email input field.
        phone_input (str): Selector for the phone input field.
        address_street_1_input (str): Selector for the first line of the street address.
        address_street_2_input (str): Selector for the second line of the street address.
        city_input (str): Selector for the city input field.
        state_province_input (str): Selector for the state/province input field.
        postal_code_input (str): Selector for the postal code input field.
        country_input (str): Selector for the country input field.
        submit_button (str): Selector for the submit button to save the contact.
        cancel_button (str): Selector for the cancel button to discard changes.
    """
    first_name_input: str = "[id='firstName']"
    last_name_input: str = "[id='lastName']"
    birthdate_input: str = "[id='birthdate']"
    email_input: str = "[id='email']"
    phone_input: str = "[id='phone']"
    address_street_1_input: str = "[id='street1']"
    address_street_2_input: str = "[id='street2']"
    city_input: str = "[id='city']"
    state_province_input: str = "[id='stateProvince']"
    postal_code_input: str = "[id='postalCode']"
    country_input: str = "[id='country']"
    submit_button: str = "[id='submit']"
    cancel_button: str = "[id='cancel']"


class ContactDetailsPageLocators:
    """
    Locators for the Contact Details Page elements.

    Attributes:
        edit_contact_button (str): Selector for the button to edit the contact details.
        delete_contact_button (str): Selector for the button to delete the contact.
        return_to_contact_list_button (str): Selector for the button to return to the contact list page.
        contact_details_form (str): Selector for the fields related to contact details.
    """
    edit_contact_button = "[id='edit-contact']"
    delete_contact_button = "[id='delete']"
    return_to_contact_list_button = "[id='return']"
    contact_details_form = "[id='contactDetails'] p span"


class EditContactPageLocators:
    """
    Locators for the Edit Contact Page elements.

    Attributes:
        first_name_input (str): Selector for the first name input field.
        last_name_input (str): Selector for the last name input field.
        birthdate_input (str): Selector for the birthdate input field.
        email_input (str): Selector for the email input field.
        phone_input (str): Selector for the phone input field.
        address_street_1_input (str): Selector for the first line of the street address.
        address_street_2_input (str): Selector for the second line of the street address.
        city_input (str): Selector for the city input field.
        state_province_input (str): Selector for the state/province input field.
        postal_code_input (str): Selector for the postal code input field.
        country_input (str): Selector for the country input field.
        submit_button (str): Selector for the submit button to save the contact.
        cancel_button (str): Selector for the cancel button to discard changes.
    """
    first_name_input: str = "[id='firstName']"
    last_name_input: str = "[id='lastName']"
    birthdate_input: str = "[id='birthdate']"
    email_input: str = "[id='email']"
    phone_input: str = "[id='phone']"
    address_street_1_input: str = "[id='street1']"
    address_street_2_input: str = "[id='street2']"
    city_input: str = "[id='city']"
    state_province_input: str = "[id='stateProvince']"
    postal_code_input: str = "[id='postalCode']"
    country_input: str = "[id='country']"
    submit_button: str = "[id='submit']"
    cancel_button: str = "[id='cancel']"
