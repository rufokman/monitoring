function sendValid() {
    const weight = document.querySelectorAll("[id$='weight']");
	const method = document.querySelectorAll("[id$='method']");
	const low = document.querySelectorAll("[id$='low_level']");
	const target = document.querySelectorAll("[id$='target_level']");
	const high = document.querySelectorAll("[id$='high_level']");
	const role = document.querySelectorAll("[id$='role']");
	const organization = document.querySelectorAll("[id$='organization']");
	const fio = document.querySelectorAll("[id$='fio']");
	const name = document.querySelectorAll("[id$='name']");
	const verificator = document.querySelectorAll("[id$='verificator']");
	const status = document.querySelectorAll("[id$='status']");
	const reason = document.querySelectorAll("[id$='reason']");
	const measure = document.querySelectorAll("[id$='measure']");
	const forecast = document.querySelectorAll("[id$='forecast']");
	const send = document.querySelectorAll("[id$='send']");
	const comment = document.querySelectorAll("[id$='comment_func']");
    let all_ok = true;
	for (let i = 0; i < weight.length; i++) {
    var reg = /^[\d\,\.]*$/;
    let weight_item = weight[i]
    let method_item = method[i]
    let low_item = low[i]
    let target_item = target[i]
    let high_item = high[i]
    let role_item = role[i]
    let organization_item = organization[i]
	let fio_item = fio[i]
	let name_item = name[i]
	let verificator_item = verificator[i]
	let status_item = status[i]
	let reason_item = reason[i]
	let measure_item = measure[i]
	let forecast_item = forecast[i]
	let send_item = send[i].checked
	let comment_func_item = comment[i]

	if (method_item.value.toString()=="" && i == weight.length-1) {
		console.log("new row")

		} else {
		let changed_organization = array_organizations[i] != organization_item.value.toString()
		let changed_role = array_roles[i] != role_item.value.toString()
        let changed_fio = array_fio[i] != fio_item.value.toString()
        let changed_name = array_names[i] != name_item.value.toString()
        let changed_method = array_methods[i] != method_item.value.toString()
        let changed_low = array_low[i] != low_item.value.toString()
        let changed_target = array_target[i] != target_item.value.toString()
        let changed_high = array_high[i] != high_item.value.toString()
        let changed_weight = array_weight[i] != weight_item.value.toString()
        let changed_verificator = array_verificator[i] != verificator_item.value.toString()
		let changed_reason = array_reason[i] != reason_item.value.toString()
		let changed_measure = array_measure[i] != measure_item.value.toString()
		let changed_forecast = array_forecast[i] != forecast_item.value.toString()
        let changed_comment_func = array_comment_func[i] != comment_func_item.value.toString()
        let form_has_changed = changed_organization ||changed_role || changed_fio || changed_name || changed_method || changed_low || changed_target || changed_high || changed_weight || changed_verificator || changed_reason || changed_measure || changed_forecast || changed_comment_func
		console.log(form_has_changed)

		let required_organization = organization_item.value.toString()==""
		let required_role = role_item.value.toString()==""
		let required_fio = fio_item.value.toString()==""
		let required_name = name_item.value.toString()==""
		let required_method = method_item.value.toString()==""
		let required_weight = weight_item.value.toString()==""
		let required_target = target_item.value.toString()==""
		let required_verificator = verificator_item.value.toString()==""

		if (form_has_changed && status_item.getAttribute("value") == 1 && send_item) {
		    alert("Внесение изменений в КПЭ, находящихся на проверке СУП, недоступно. Изменения будут сброшены.")
		}

		if (form_has_changed == false && status_item.getAttribute("value") == 0 && send_item) {
		    alert("Повторная отправка на согласование возможна только в случае внесения изменений в КПЭ. Обратитесь к сотруднику СУП УК")
		}

		if (required_organization || required_role || required_fio ||required_name
		 	|| required_method || required_target || required_weight || required_verificator) {
			alert("Заполните все обязательные поля.");
			if (required_organization) {
				organization_item.style.borderColor = "red"
			}
		}

	}
	}

};