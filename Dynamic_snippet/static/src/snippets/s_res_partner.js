
odoo.define('test_highlight_partners.highlight_snippet', function (require) {
    'use strict';

    const publicWidget = require('web.public.widget');

    publicWidget.registry.HighlightPartnerSnippet = publicWidget.Widget.extend({
        selector: '.s_highlight_partners',
        start: function () {
            const partnerIds = this.$el.data('partners').split(',');
            this._rpc({
                route: '/partners/highlighted',
                params: {},
//                model: 'res.partner',
//                method: 'search_read',
//                domain: [['id', 'in', partnerIds], [' highlight_partner', '=', true]],
//                fields: ['name'],
            }).then(partners => {
                this.$el.empty();
                partners.forEach(partner => {
                    this.$el.append(`<div class="highlighted-partner">${partner.name}</div>`);
                });
            });
        }
    });
});