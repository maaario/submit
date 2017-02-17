from django.conf import settings as django_settings

SUBMIT_TASK_MODEL = getattr(django_settings, 'SUBMIT_TASK_MODEL', 'submit.BaseTask')

SUBMIT_PATH = getattr(django_settings, 'SUBMIT_PATH', 'submit/')

SUBMIT_VIEWABLE_EXTENSIONS = getattr(django_settings, 'SUBMIT_VIEWABLE_EXTENSIONS', ('.pdf', '.txt'))

JUDGE_INTERFACE_IDENTITY = getattr(django_settings, 'JUDGE_INTERFACE_IDENTITY', 'TESTOVAC')
JUDGE_ADDRESS = getattr(django_settings, 'JUDGE_ADDRESS', '127.0.0.1')
JUDGE_PORT = getattr(django_settings, 'JUDGE_PORT', 12347)
# SubmitReceiver object may not be in database yet when this function is called
JUDGE_DEFAULT_INPUTS_FOLDER_FOR_RECEIVER = getattr(django_settings, 'JUDGE_DEFAULT_INPUTS_FOLDER_FOR_RECEIVER',
                                                   'submit.defaults.default_inputs_folder_at_judge')

SUBMIT_IS_SUBMIT_ACCEPTED = getattr(django_settings, 'SUBMIT_IS_SUBMIT_ACCEPTED', 'submit.defaults.is_submit_accepted')
SUBMIT_FORM_SUCCESS_MESSAGE = getattr(django_settings, 'SUBMIT_FORM_SUCCESS_MESSAGE',
                                      'submit.defaults.form_success_message')

# Format of displayed score can depend on other models
SUBMIT_PREFETCH_DATA_FOR_SCORE_CALCULATION = getattr(django_settings,
                                                     'SUBMIT_PREFETCH_DATA_FOR_SCORE_CALCULATION',
                                                     'submit.defaults.prefetch_data_for_score_calculation')
SUBMIT_DISPLAY_SCORE = getattr(django_settings, 'SUBMIT_DISPLAY_SCORE', 'submit.defaults.display_score')
SUBMIT_RENDER_REVIEW_COMMENT = getattr(django_settings, 'SUBMIT_RENDER_REVIEW_COMMENT',
                                       'submit.defaults.render_review_comment')

# Override `SubmitReceiver.__str__()` to be more descriptive than '{}'.format(id)
SUBMIT_DISPLAY_SUBMIT_RECEIVER_NAME = getattr(django_settings, 'SUBMIT_DISPLAY_SUBMIT_RECEIVER_NAME',
                                              'submit.defaults.display_submit_receiver_name')

# Override these functions to set access rights for receivers
SUBMIT_CAN_POST_SUBMIT = getattr(django_settings, 'SUBMIT_CAN_POST_SUBMIT',
                                 'submit.defaults.can_post_submit')
SUBMIT_HAS_ADMIN_PRIVILEGES_FOR_RECEIVER = getattr(django_settings, 'SUBMIT_HAS_ADMIN_PRIVILEGES_FOR_RECEIVER',
                                                   'submit.defaults.has_admin_privileges_for_receiver')

SUBMIT_RECEIVER_TEMPLATES = getattr(django_settings, 'SUBMIT_RECEIVER_TEMPLATES', {
    'Source': {
        'has_form': True,
        'caption': 'Source',
        'extensions': '',
        'languages': 'cc, pas, c, py, hs, cs, java',
        'external_link': '',
        'send_to_judge': True,
        'inputs_folder_at_judge': '',
        'show_all_details': False,
        'show_submitted_file': True,
    },
    'Testable ZIP': {
        'has_form': True,
        'caption': 'Testable ZIP',
        'extensions': '',
        'languages': 'zip',
        'external_link': '',
        'send_to_judge': True,
        'inputs_folder_at_judge': '',
        'show_all_details': True,
        'show_submitted_file': False,
    },
    'Description': {
        'has_form': True,
        'caption': 'Description',
        'extensions': '',
        'languages': '',
        'external_link': '',
        'send_to_judge': False,
        'inputs_folder_at_judge': '',
        'show_all_details': False,
        'show_submitted_file': False,
    },
    'Link': {
        'has_form': False,
        'caption': '',
        'extensions': '',
        'languages': '',
        'external_link': '',
        'send_to_judge': False,
        'inputs_folder_at_judge': '',
        'show_all_details': False,
        'show_submitted_file': False,
    },
})
