import { PosOrderline } from "@point_of_sale/app/models/pos_order_line";

import { patch } from "@web/core/utils/patch";


patch(PosOrderline.prototype, {

    getDisplayData() {

        return {

            ...super.getDisplayData(),

            default_code: this.product_id.default_code,

        };

    },

});