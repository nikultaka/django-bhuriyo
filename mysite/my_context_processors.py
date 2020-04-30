
from preferences import preferences

def layout_data(request):
    portal_contact_home_about = preferences.MyPreferences.portal_contact_home_about
    portal_contact_facebook = preferences.MyPreferences.portal_contact_facebook
    portal_contact_instagram = preferences.MyPreferences.portal_contact_instagram
    portal_contact_twitter = preferences.MyPreferences.portal_contact_twitter
    portal_contact_email = preferences.MyPreferences.portal_contact_email
    portal_contact_phone = preferences.MyPreferences.portal_contact_phone
    portal_contact_address = preferences.MyPreferences.portal_contact_address
    return {"portal_contact_home_about":portal_contact_home_about,"portal_contact_facebook":portal_contact_facebook,"portal_contact_instagram":portal_contact_instagram,"portal_contact_twitter":portal_contact_twitter,"portal_contact_email":portal_contact_email,"portal_contact_phone":portal_contact_phone,"portal_contact_address":portal_contact_address}



