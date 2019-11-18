style: {
        shape: 'rect',
        color: ‘white’,
        layout: 'vertical',
        label: 'paypal',
        
    },
    
    createOrder: function(data, actions) {
        return actions.order.create({
            purchase_units: [{
                amount: { 
                    value: ‘5’
                }
            }]
        });
    },
    onApprove: function(data, actions) {
        return actions.order.capture().then(function(details) {
            alert('Transaction completed by ' + details.payer.name.given_name + '!');
            
            
            )
            return fetch(‘http://localhost:5000/approved');

        });
    }
}).render('#paypal-button-container','#payP');
