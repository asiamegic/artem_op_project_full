from selenium.webdriver.common.by import By


class Locator:
    sign_in_button = (By.XPATH, "//span[contains(text(),'Sign in')]")

    username = (By.XPATH, "//input[@id='username-pulldown']")

    password = (By.XPATH, "//input[@id='password-pulldown']")

    login = (By.XPATH, "//input[@id='login-pulldown']")

    project_button = (By.XPATH, "//span[@class='button--text'][normalize-space()='Project']")

    project_name = (By.XPATH, "//input[@id='formly_3_textInput_name_0']")

    name = (By.XPATH, "//input[@id='formly_3_textInput_name_0']")

    # driver.find_element(By.XPATH, "//input[@id='formly_3_textInput_name_0']").clear()
    name1 = (By.XPATH, "//input[@id='formly_3_textInput_name_0']")

    advanced_setting = (By.XPATH, "//button[contains(text(),'Advanced settings')]")

    advance_validation = (By.XPATH,
                          "//body//div[@id='wrapper']//formly-field//formly-field[2]//op-dynamic-field-wrapper[1]//op-form-field[1]//label[1]//div[1]")

    description = (By.XPATH,
                   "//body/div[@id='wrapper']/div[@id='main']/main[@id='content-wrapper']/div[@id='content']/openproject-base[1]/div[1]/ui-view[1]/op-new-project[1]/op-dynamic-form[1]/form[1]/formly-form[1]/formly-field[3]/op-dynamic-field-group-wrapper[1]/fieldset[1]/div[1]/formly-group[1]/formly-field[2]/op-dynamic-field-wrapper[1]/op-form-field[1]/div[2]/op-formattable-textarea-input[1]/op-formattable-control[1]/div[1]/op-ckeditor[1]/div[1]/div[2]/div[1]/p[1]")

    status_button = (By.XPATH,
                     "//body/div[@id='wrapper']/div[@id='main']/main[@id='content-wrapper']/div[@id='content']/openproject-base[1]/div[1]/ui-view[1]/op-new-project[1]/op-dynamic-form[1]/form[1]/formly-form[1]/formly-field[3]/op-dynamic-field-group-wrapper[1]/fieldset[1]/div[1]/formly-group[1]/formly-field[5]/op-dynamic-field-wrapper[1]/op-form-field[1]/label[1]/div[3]/op-select-project-status-input[1]/ng-select[1]/div[1]/span[1]")

    on_track = (By.XPATH, "//span[contains(text(),'On track')]")

    save = (By.XPATH, "//button[contains(text(),'Save')]")

    projectname = (By.XPATH, "//span[@class='op-app-menu--item-title ellipsis']")

    search_type = (By.XPATH, "//input[@id='project_autocompletion_input']")

    drop = (By.XPATH, "//*[@id='ui-id-1']/li")

    drop_click = (By.XPATH, "//li[@id='project-search-container']//a[1]")

    search = (By.XPATH, "//a[@id='main-menu-work-packages']")

    table = (By.XPATH,
             "//*[@id='content']/openproject-base/div/ui-view/openproject-base/div/ui-view/work-packages-base/div/ui-view/wp-view-page/div/div[3]/div[1]/wp-list-view/wp-table/div/div[1]/table")

    rowcount = (By.XPATH,
                "//*[@id='content']/openproject-base/div/ui-view/openproject-base/div/ui-view/work-packages-base/div/ui-view/wp-view-page/div/div[3]/div[1]/wp-list-view/wp-table/div/div[1]/table/tbody[1]/tr")
    workpackage = (By.XPATH, "//div[@class='wp-create-button']")

    menu = (By.XPATH, "//a[@aria-label='Task']//span[contains(text(),'Task')]")

    value1 = (By.XPATH,
              "//div[@class='inline-edit--container status wp-new-top-row--status -no-label']//div//span[@title='New'][normalize-space()='New']")

    value2 = (By.XPATH,
              "//div[@class='inline-edit--container type wp-new-top-row--type -no-label']//div//span[@title='Task'][normalize-space()='Task']")

    package_name = (By.XPATH, "//input[@id='wp-new-inline-edit--field-subject']")

    package_des = (By.XPATH, "//div[@aria-label='Rich Text Editor, main']")

    save_button = (By.XPATH, "//button[@id='work-packages--edit-actions-save']")

    rowcount1 = (By.XPATH,
                 "//*[@id='content']/openproject-base/div/ui-view/openproject-base/div/ui-view/work-packages-base/div/ui-view/wp-view-page/div/div[3]/div[1]/wp-list-view/wp-table/div/div[1]/table/tbody[1]/tr")

    value3 = (By.XPATH,
              "//*[@id='content']/openproject-base/div/ui-view/openproject-base/div/ui-view/work-packages-base/div/ui-view/wp-view-page/div/div[3]/div[2]/wp-split-view-entry/div/div[1]/edit-form/div[1]/div/wp-subject/div/div[1]/editable-attribute-field/div/div[2]/span")

    value4 = (By.XPATH,
              "//*[@id='content']/openproject-base/div/ui-view/openproject-base/div/ui-view/work-packages-base/div/ui-view/wp-view-page/div/div[3]/div[2]/wp-split-view-entry/div/div[1]/edit-form/div[1]/div/wp-subject/div/div[2]/editable-attribute-field/div/div[2]/span")
