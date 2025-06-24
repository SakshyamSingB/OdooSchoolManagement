/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { renderToElement } from '@web/core/utils/render';
import { jsonrpc } from "@web/core/network/rpc_service";

publicWidget.registry.ShowGrades = publicWidget.Widget.extend({
    selector: '#show_grades_section',

    async start() {
        console.log('Fetching grades...');

        try {
            const grades = await jsonrpc('/school_management/api/grades', {});


            console.log('Grades received:', grades);
            // debugger
            const rendered = renderToElement('school_management.grade_template', {grades});
            // const rendered = renderToElement('school_management.test');
            this.$el.find('#grades_list').html(rendered.innerHTML);
        } catch (err) {
            console.error('Error fetching grades:', err);
            this.$el.find('#grades_list').html('<p>Failed to load grades.</p>');
        }
    },
});
