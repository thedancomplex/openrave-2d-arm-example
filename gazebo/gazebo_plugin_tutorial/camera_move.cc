#include <boost/bind.hpp>
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>
#include <gazebo/transport/transport.hh>

    namespace gazebo
    {     
      class CameraMove : public ModelPlugin
      {     
        public: CameraMove() : ModelPlugin() {}

    public: void Load(physics::ModelPtr _parent, sdf::ElementPtr /*_sdf*/)
    {
      // Store the pointer to the model
      this->model = _parent;

      // Listen to the update event. This event is broadcast every
      // simulation iteration.
      this->updateConnection = event::Events::ConnectWorldUpdateBegin(
          boost::bind(&CameraMove::OnUpdate, this, _1));
    }      

        // OnUpdate will not be executed unless it's explicitly connected by
        //   an event, e.g. use event::Events::ConnectWorldUpdateStart
        public: void OnUpdate()
        { 
          math::Vector3 v(0.03, 0, 0);
          math::Pose pose = this->model->GetWorldPose();
          v = pose.rot * v;

          // Apply a small linear velocity to the model. 
          this->model->SetLinearVel(v);
          this->model->SetAngularVel(math::Vector3(0, 0, 0.01));
        } 

        // Pointer to the model
        private: physics::ModelPtr model;

        // Pointer to the update event connection
        private: event::ConnectionPtr updateConnection;
      };

      // Register this plugin with the simulator
      GZ_REGISTER_MODEL_PLUGIN(CameraMove)
    }
